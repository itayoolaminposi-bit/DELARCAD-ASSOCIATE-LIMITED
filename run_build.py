import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from build import page
from content_home import HOME_BODY
from content_about_us import ABOUT_US_BODY
from content_about_practice import ABOUT_PRACTICE_BODY
from content_resources import RESOURCES_BODY
from content_how_it_works import HOW_IT_WORKS_BODY
from content_get_started import GET_STARTED_BODY
from content_contact import CONTACT_BODY

page("index.html", "Home",
     "Delarcad Associate Limited is an architecture and design practice working across residential, civic and commercial projects from Lagos, London and Toronto.",
     HOME_BODY)

page("about-us.html", "About Us",
     "Meet the principals and studios of Delarcad Associate Limited, an architecture practice with teams in Lagos, London and Toronto.",
     ABOUT_US_BODY)

page("about-delarcad.html", "The Practice",
     "The history, mission and track record of Delarcad Associate Limited, founded in Lagos in 2011.",
     ABOUT_PRACTICE_BODY)

page("resources.html", "Resources",
     "Guides and checklists for clients planning a residential, civic or commercial building project.",
     RESOURCES_BODY)

page("how-it-works.html", "How It Works",
     "The six-stage process Delarcad Associate Limited follows on every project, from discovery call to construction administration.",
     HOW_IT_WORKS_BODY)

page("get-started.html", "Start a Project",
     "Tell Delarcad Associate Limited about your site and project so we can schedule a discovery call.",
     GET_STARTED_BODY)

page("contact.html", "Contact",
     "Contact details for Delarcad Associate Limited's studios in Lagos, London and Toronto.",
     CONTACT_BODY)

print("Build complete.")
