import os
from pynamodb.models import Model
from pynamodb.attributes import NumberAttribute


class Post:
    def __init__(self, post_id, title, published_date):
        self.post_id = post_id
        self.title = title.strip()
        self.published_date = published_date

    @property
    def link(self):
        return f'https://ara.kaist.ac.kr/board/Food/{self.post_id}'

    @property
    def text(self):
        return f'{self.published_date.strftime("%Y-%m-%d")}에 게시됨: {self.title}\n자세한 내용은 {self.link} 에서 확인하세요.'


class Chat(Model):
    class Meta:
        table_name = os.environ.get('CHATS_DYNAMODB_TABLE')
        region = os.environ.get('AWS_REGION')
        write_capacity_units = 1
        read_capacity_units = 1

    chat_id = NumberAttribute(hash_key=True)


if not Chat.exists():
    Chat.create_table(wait=True)
