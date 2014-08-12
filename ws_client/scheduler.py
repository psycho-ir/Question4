__author__ = 'soroosh'
from easy_scheduler.simple_scheduler import SimpleThreadScheduler
from datetime import datetime, timedelta
from views import sessions


def clean_expired_session():
    print 'Finding expires sessions...'
    for session_id in sessions.keys():
        session_date = sessions[session_id]
        threshold = datetime.now() - timedelta(minutes=10)
        if session_date < threshold:
            del sessions[session_id]
            print ('Session: %s removed' % session_id)

    print 'Expired session removed.'


scheduler = SimpleThreadScheduler(300, clean_expired_session)
scheduler.run()
