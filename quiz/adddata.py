import json
from datetime import datetime
from django.utils.dateparse import parse_datetime
from quiz.models import Question, Choice  # เปลี่ยนชื่อแอป quiz ตามของคุณ

def import_quizzes(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        # สร้างหรืออัพเดต Question
        question, created = Question.objects.update_or_create(
            id=item['id'],
            defaults={
                'text': item['text'],
                'published_date': parse_datetime(item['published_date'])
            }
        )

        # สร้างหรืออัพเดต Choices
        choices_data = item.get('choices', [])
        for choice_data in choices_data:
            Choice.objects.update_or_create(
                id=choice_data['id'],
                defaults={
                    'question': question,
                    'text': choice_data['text'],
                    'correct': choice_data['correct']
                }
            )

# เรียกใช้ฟังก์ชันนี้โดยใส่ path ของไฟล์ JSON
# import_quizzes('path/to/quizzes-1-68.json')
