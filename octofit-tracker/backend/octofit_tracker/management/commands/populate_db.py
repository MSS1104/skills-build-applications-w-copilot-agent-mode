from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from djongo import models

from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()


        # Create users
        tony = User.objects.create_user(username='ironman', email='tony@marvel.com', password='password', first_name='Tony', last_name='Stark')
        bruce = User.objects.create_user(username='hulk', email='bruce@marvel.com', password='password', first_name='Bruce', last_name='Banner')
        clark = User.objects.create_user(username='superman', email='clark@dc.com', password='password', first_name='Clark', last_name='Kent')
        diana = User.objects.create_user(username='wonderwoman', email='diana@dc.com', password='password', first_name='Diana', last_name='Prince')

        # Create teams with members_emails
        marvel = Team.objects.create(name='Marvel', members_emails=[tony.email, bruce.email])
        dc = Team.objects.create(name='DC', members_emails=[clark.email, diana.email])

        # Create activities
        Activity.objects.create(user=tony, type='run', duration=30, calories=300)
        Activity.objects.create(user=bruce, type='swim', duration=45, calories=400)
        Activity.objects.create(user=clark, type='fly', duration=60, calories=500)
        Activity.objects.create(user=diana, type='fight', duration=50, calories=450)

        # Create workouts
        Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', duration=40)
        Workout.objects.create(name='Strength Training', description='Strength for all heroes', duration=60)

        # Create leaderboard
        Leaderboard.objects.create(user=tony, score=1000)
        Leaderboard.objects.create(user=bruce, score=900)
        Leaderboard.objects.create(user=clark, score=1100)
        Leaderboard.objects.create(user=diana, score=1050)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
