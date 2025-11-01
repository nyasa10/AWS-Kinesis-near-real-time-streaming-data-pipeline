# AWS Kinesis Near-Real-Time Streaming Data Pipeline

A **serverless, near-real-time data pipeline** that captures, transforms, and stores streaming order data using AWS services. This project demonstrates **Change Data Capture (CDC)** from DynamoDB, **event-driven routing**, **record transformation**, and **analytics-ready storage** — all in a scalable and cost-efficient architecture.

# Tech stack and AWS services used: 
```text
-Python
-S3
-DynamoDB
-Kinesis
-Lambda
-Athena
-Glue
-CloudWatch
-Ubuntu
```

```mermaid
graph TD
    A[Mock Data Generator<br><code>mock_data_generator_for_dynamodb.py</code>] --> B[DynamoDB Table<br><code>OrderTable</code>]
    B -->|DynamoDB Streams<br>CDC| C[EventBridge Pipe]
    C --> D[Kinesis Data Stream<br><code>order-stream</code>]
    D --> E[Kinesis Firehose<br><code>order-firehose</code>]
    E --> F[Lambda Transformation<br><code>transformation_layer_with_lambda.py</code>]
    F --> G[S3 Bucket<br>Partitioned: year/month/day/]
    
    G --> H[AWS Glue<br>Data Catalog + Schema]
    H --> I[Amazon Athena<br>SQL Queries]

    style A fill:#2ecc71, color:white
    style B fill:#3498db, color:white
    style C fill:#9b59b6, color:white
    style D fill:#e67e22, color:white
    style E fill:#e74c3c, color:white
    style F fill:#f1c40f, color:white
    style G fill:#1abc9c, color:white
    style H fill:#34495e, color:white
    style I fill:#8e44ad, color:white
