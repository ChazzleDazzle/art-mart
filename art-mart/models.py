class Art(object):
    def __init__(
        self,
        author=None,
        title=None,
        medium=None,
        img_name=None,
        background_color=None,
        date_produced=None,
        price=None,
        high_bidder=None,
    ):
        self.author = author
        self.title = title
        self.medium = medium
        self.img_name = img_name
        self.background_color = background_color
        self.date_produced = date_produced
        self.price = price
        self.high_bidder = high_bidder

    def __admin_set_price(self, admin_price, admin_high_bidder=None):
        self.price = admin_price
        self.high_bidder = admin_high_bidder

    def update_price(self, new_price, bidder):
        self.price = new_price
        self.high_bidder = bidder

    def determine_high_bid(self, bid, bidder):
        if self.price:
            if self.price < bid:
                update_price(bid, bidder)

    def validate_bidder(self, bidder):
        # TODO: Parse database for users.  If valid user, return True, else False.
        return True

    def get_background_color(self, background_color=None):
        # TODO: Is there a way to process a photo, and get a background color?
        # Return black for now.
        return (255, 255, 255)

