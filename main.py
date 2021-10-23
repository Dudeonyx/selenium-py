from booking.booking import Booking


with Booking() as bot:
    bot.land_first_page()
    bot.change_currency('USD')
    bot.select_place_to_go('New York')
    bot.print_page_as_pdf('test_page')
    print('exiting...')
