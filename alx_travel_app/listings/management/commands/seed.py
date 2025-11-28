from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing, Booking, Review

from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = "Seed the database with Listings, Bookings, and Reviews"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Seeding database..."))

        # ------------------------------------------------------------
        # 1. Create demo users
        # ------------------------------------------------------------
        users = []
        usernames = ["alice", "bob", "charlie"]

        for username in usernames:
            user, created = User.objects.get_or_create(
                username=username,
                defaults={"email": f"{username}@example.com"}
            )
            if created:
                user.set_password("password123")
                user.save()
            users.append(user)

        # ------------------------------------------------------------
        # 2. Create Listings
        # ------------------------------------------------------------
        listings_data = [
            {
                "title": "Beachfront Villa",
                "description": "A beautiful villa next to the sea.",
                "location": "Malibu, California",
                "price_per_night": 450.00,
            },
            {
                "title": "Mountain Cabin",
                "description": "Rustic cabin with scenic mountain views.",
                "location": "Aspen, Colorado",
                "price_per_night": 250.00,
            },
            {
                "title": "City Apartment",
                "description": "Modern apartment in the heart of the city.",
                "location": "New York, NY",
                "price_per_night": 300.00,
            },
        ]

        listings = []

        for item in listings_data:
            listing, _ = Listing.objects.get_or_create(
                title=item["title"],
                defaults={
                    "description": item["description"],
                    "location": item["location"],
                    "price_per_night": item["price_per_night"],
                    "available": True,
                }
            )
            listings.append(listing)

        # ------------------------------------------------------------
        # 3. Create Bookings
        # ------------------------------------------------------------
        bookings = []

        for i in range(5):
            user = random.choice(users)
            listing = random.choice(listings)

            check_in = date.today() + timedelta(days=random.randint(1, 10))
            check_out = check_in + timedelta(days=random.randint(2, 7))

            total_price = (check_out - check_in).days * listing.price_per_night

            booking = Booking.objects.create(
                user=user,
                listing=listing,
                check_in=check_in,
                check_out=check_out,
                total_price=total_price
            )
            bookings.append(booking)

        # ------------------------------------------------------------
        # 4. Create Reviews — one per booking (optional)
        # ------------------------------------------------------------
        for booking in bookings:
            Review.objects.get_or_create(
                booking=booking,
                defaults={
                    "rating": random.randint(3, 5),
                    "comment": "Great stay! Would recommend."
                }
            )

        self.stdout.write(self.style.SUCCESS("Database seeding complete!"))
