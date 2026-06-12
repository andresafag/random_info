FROM public.ecr.aws/lambda/python:3.11

COPY requirements.txt ${LAMBDA_TASK_ROOT}/
RUN pip install --no-cache-dir -r requirements.txt

COPY application.py ${LAMBDA_TASK_ROOT}/
COPY static/ ${LAMBDA_TASK_ROOT}/static/
COPY templates/ ${LAMBDA_TASK_ROOT}/templates/

CMD [ "application.handler" ]