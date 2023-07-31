from Booking.booking import Booking

with Booking(teardown=True) as bot:
    bot.landing_first_page()
