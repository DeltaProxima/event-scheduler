# Generated by Django 3.2.3 on 2022-03-10 17:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='date',
            field=models.DateField(default=django.utils.timezone.localdate),
        ),
        migrations.AlterField(
            model_name='club',
            name='club_name',
            field=models.CharField(choices=[('0', 'Select'), ('SWC', 'SWC'), ('ACADEMIC INITIATIVE CLUB', 'ACADEMIC INITIATIVE CLUB'), ('ACUMEN CLUB', 'ACUMEN CLUB'), ('AEROMODELLING CLUB', 'AEROMODELLING CLUB'), ('AI CLUB', 'AI CLUB'), ('ALCHER', 'ALCHER'), ('ANCHORENZA CLUB', 'ANCHORENZA CLUB'), ('ASTRO CLUB', 'ASTRO CLUB'), ('ATHLETICS CLUB', 'ATHLETICS CLUB'), ('AQUATICS CLUB', 'AQUATICS CLUB'), ('AUTOMOBILE CLUB', 'AUTOMOBILE CLUB'), ('BADMINTON CLUB', 'BADMINTON CLUB'), ('BASKETBALL CLUB', 'BASKETBALL CLUB'), ('CODING CLUB', 'CODING CLUB'), ('CA CLUB', 'CA CLUB'), ('CCD CLUB', 'CCD CLUB'), ('CRICKET CLUB', 'CRICKET CLUB'), ('DANCE CLUB', 'DANCE CLUB'), ('DRAMA CLUB', 'DRAMA CLUB'), ('EE CLUB', 'EE CLUB'), ('ED CLUB', 'ED CLUB'), ('FNC CLUB', 'FNC CLUB'), ('FINE ARTS CLUB', 'FINE ARTS CLUB'), ('FOOTBALL CLUB', 'FOOTBALL CLUB'), ('HOCKEY CLUB', 'HOCKEY CLUB'), ('LITERARY CLUB', 'LITERARY CLUB'), ('MOVIE CLUB', 'MOVIE CLUB'), ('MUSIC CLUB', 'MUSIC CLUB'), ('PHOTOGRAPHY CLUB', 'PHOTOGRAPHY CLUB'), ('PRAKRITI CLUB', 'PRAKRITI CLUB'), ('RADIOG CLUB', 'RADIOG CLUB'), ('RED RIBBON CLUB', 'RED RIBBON CLUB'), ('RIGHTS AND RESPONSIBILITIES CLUB', 'RIGHTS AND RESPONSIBILITIES CLUB'), ('ROBOTICS CLUB', 'ROBOTICS CLUB'), ('SAATHI COUNSELLING CLUB', 'SAATHI COUNSELLING CLUB'), ('SAIL', 'SAIL'), ('SOCIAL SERVICE CLUB', 'SOCIAL SERVICE CLUB'), ('SQUASH CLUB', 'SQUASH CLUB'), ('TABLE TENNIS CLUB', 'TABLE TENNIS CLUB'), ('TECHNICHE', 'TECHNICHE'), ('TENNIS CLUB', 'TENNIS CLUB'), ('UG CLUB', 'UG CLUB'), ('VOLLEYBALL CLUB', 'VOLLEY BALL CLUB'), ('WEIGHTLIFTING CLUB', 'WEIGHTLIFTING CLUB'), ('YOUTH EMPOWERMENT CLUB', 'YOUTH EMPOWERMENT CLUB')], max_length=50),
        ),
        migrations.AlterField(
            model_name='club',
            name='title',
            field=models.CharField(default='None', max_length=50),
        ),
    ]