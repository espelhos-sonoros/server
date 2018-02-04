from .dao import *
from .services import *
from .utils import *

def espelhos_sonoros(app, socketio, db):
    app.logger.info('Creating application.')
    queue_dao = QueueDAO(db)
    video_dao = VideoDAO(app.config)
    audio_dao = AudioDAO(app.config)

    app.logger.info('Created models')
    db.create_all()

    app.logger.info('Created database')

    oauth_service(app)
    twitter_service = TwitterService(app)
    video_service(app, socketio, audio_dao, video_dao)

    templates_service(app, twitter_service)

    app.logger.info('Created services')
