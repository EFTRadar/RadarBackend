from fastapi import APIRouter
import random
import string
from mongo import db
import secrets
from endpoints.api.v1.create_session.methods.response_type import SessionResponse

router = APIRouter()


@router.get('/')
def create_session():
    sessions = db['sessions']

    while True:
        session_id = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=8))

        if sessions.find({'sessionId': session_id}) is None:
            break

    authentication_uuid = secrets.token_hex(64)
    sessions.insert_one({
        'sessionId': session_id,
        'authenticationUuid': authentication_uuid
    })

    return SessionResponse(
        session_id=session_id,
        authentication_token=authentication_uuid
    )
