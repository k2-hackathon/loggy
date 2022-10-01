#!/usr/bin/env bash

aws dynamodb \
--region ap-northeast-1 \
--endpoint-url http://dynamodb:8000 \
create-table \
--table-name Geography \
--attribute-definitions \
AttributeName=user_id,AttributeType=S AttributeName=timestamp,AttributeType=N \
--key-schema \
AttributeName=user_id,KeyType=HASH AttributeName=timestamp,KeyType=RANGE \
--provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
--billing-mode PAY_PER_REQUEST