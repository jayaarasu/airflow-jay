FROM apache/airflow:2.9.1

USER root

COPY dist/data_pipeline_lib-1.0.0-py3-none-any.whl /tmp/

RUN pip install /tmp/data_pipeline_lib-1.0.0-py3-none-any.whl

USER airflow