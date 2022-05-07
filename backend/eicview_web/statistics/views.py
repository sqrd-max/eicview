from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for


mod = Blueprint('statistics', __name__, url_prefix='/statistics')


@mod.route('/')
def index():

    return render_template("statistics/index.html",
                           number_of_files=15934,
                           total_space="154Mb")
    pass
