from const import *
import requests


def set_typetalk_talkName(talk_name: str, user_postid: int) -> int:
    """
    Create a Typetalk tag and post the PostID you add to the tag.
    https://developer.nulab.com/docs/typetalk/api/1/create-talk/

    :param talk_name: Tag name.
    :param user_postid: Post ID that you want to add to the tag.
    :return: Talk ID.
    """

    api_endpoint = f"{TYPETALK_API_URL}/topics/{TYPETALK_TOPIC_ID}/talks"
    headers = {"X-TYPETALK-TOKEN": TYPETALK_TOKEN}

    payload = {"talkName": talk_name, "postIds[0]": user_postid}

    response = requests.post(api_endpoint, headers=headers, data=payload)
    talk_id = response.json()["talk"]["id"]

    return talk_id


def get_typetalk_talk(talk_id: int) -> list:
    """
    Get messages by tag and sort them in ascending order.
    Create a prompt in the form of a conversation history to pass to the OpenAI API.
    https://developer.nulab.com/docs/typetalk/api/1/get-talk/

    :param talk_id: Talk ID.
    :return: The prompt to pass to the OpenAI API.
    """

    # The number of messages to retrieve.
    talk_count = TYPETALK_TALK_COUNT
    # message order.
    talk_direction = TYPETALK_TAKL_DIRECTION

    api_endpoint = (
        f"{TYPETALK_API_URL}/topics/{TYPETALK_TOPIC_ID}/talks/{talk_id}/posts"
    )
    headers = {"X-TYPETALK-TOKEN": TYPETALK_TOKEN}

    payload = {"count": talk_count, "direction": talk_direction}

    response = requests.get(api_endpoint, headers=headers, params=payload)
    talk_posts = response.json()["posts"]

    # Sort messages in ascending order
    sorted_messages = sorted(talk_posts, key=lambda x: x["id"])

    prompt = []

    system = {"role": "system", "content": CHARACTER}

    for message in sorted_messages:
        text = message["message"]

        comment = {}
        if not message["account"]["isBot"]:
            comment["role"] = "user"
            comment["content"] = text

        elif message["account"]["isBot"]:
            comment["role"] = "assistant"
            comment["content"] = text

        prompt.append(comment)

    prompt.insert(0, system)

    return prompt


def post_typetalk_message(message: str, post_id: int, talk_id: int) -> str:
    """
    Post OpenAI API responses to the Typetalk topic.
    https://developer.nulab.com/docs/typetalk/api/1/post-message/

    :param message: Message to be posted to the Typetalk topic.
    :param post_id: Post ID to reply to.
    :param talk_id: Talk ID to add the message to.
    :return: JSON
    """

    headers = {"X-TYPETALK-TOKEN": TYPETALK_TOKEN}
    payload = {"message": message, "replyTo": post_id, "talkIds[0]": talk_id}

    response = requests.post(TYPETALK_API_ENDPOINT, headers=headers, data=payload)

    return response.json()
