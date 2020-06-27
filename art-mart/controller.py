#!/usr/bin/env python3

from flask import Flask, render_template
from .models import Art

app = Flask(__name__)


@app.route("/")
def sample_products():
    sample_products = [
        Art(
            author="Oliver",
            title="Mytitle",
            medium="paper and paint",
            img_name="Gazer.jpg",
            date_produced="Today",
            price=4.00,
            high_bidder="Someone",
        ),
        Art(
            author="Oliver",
            title="Mytitle",
            medium="paper and paint",
            img_name="Gazer.jpg",
            date_produced="Today",
            price=4.00,
            high_bidder="Someone",
        ),
        Art(
            author="Oliver",
            title="Mytitle",
            medium="paper and paint",
            img_name="Gazer.jpg",
            date_produced="Today",
            price=4.00,
            high_bidder="Someone",
        ),
        Art(
            author="Oliver",
            title="Mytitle",
            medium="paper and paint",
            img_name="Gazer.jpg",
            date_produced="Today",
            price=4.00,
            high_bidder="Someone",
        ),
    ]
    return render_template("base.html", items=sample_products)

