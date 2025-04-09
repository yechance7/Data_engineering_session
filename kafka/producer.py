'''
2024-2 Ybigta DE Kafka 과제
- Kafka Broker, Consumer가 AWS 위에서 실행되고 있다.
- 이 Consumer는 'homework' topic을 구독하고 있다.
- Producer를 구현한 아래의 코드를 적절하게 수정하여,
  Consumer가 메세지를 잘 받을 수 있도록 하자!
'''

# 조건 1. notion 과제에 써있는 설명을 그대로 따라한다.
# 조건 2. Producer는 'homework' topic에 메세지를 전송한다.
# 조건 3. Producer는 'messages.'txt' 파일에서 메세지를 읽어와 전송한다.
# 조건 4. Producer는 'homework' topic에 메세지를 10개만 전송한다.
# 조건 5. messages.txt 파일을 수정하지 않는다.
# 조건 6. Consumer에 도착하는 message 형태는 "번호: 메세지"이다. (eg. "1: Hello, Kafka")

from kafka import KafkaProducer
import time

# Kafka Producer 설정
bootstrap_server = '3.26.229.74' + ':9092' 
producer = KafkaProducer(bootstrap_servers=bootstrap_server)

# 파일에서 메시지 읽기
with open('messages.txt', 'r') as file:
    messages = file.readlines()

# 'homework' 토픽으로 메시지 전송
for i, message in enumerate(messages[:10]):
    formatted_message = f"{i + 1}: {message.strip()}"  # "번호: 메시지" 형식으로 포맷
    producer.send('homework', value=formatted_message.encode('utf-8'))
    print(f"Sent: {formatted_message}")  # 전송된 메시지 출력
    time.sleep(1)  # 전송 간격 조정

# Producer 닫기
producer.flush()
producer.close()
