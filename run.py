from Booking.booking import Booking

with Booking(teardown=True) as bot:
    bot.landing_first_page()
    bot.dismiss_signin_popup()
    bot.select_currency(currency='GBP')
