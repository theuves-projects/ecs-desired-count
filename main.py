import os
import json
import ecs

def handler(event, context):
    try:
        cluster = os.environ.get("CLUSTER")
        service = os.environ.get("SERVICE")
        count_order = os.environ.get("COUNT_ORDER")

        count_list = count_order.split(",")

        if len(count_list) == 0:
            return {
                "statusCode": 500,
                "body": json.dumps({"message": "COUNT_ORDER is not valid"})
            }

        desired_count = ecs.get_desired_count(cluster, service)
        next_count = ecs.get_next_count(count_list, desired_count)

        ecs.set_desired_count(cluster, service, int(next_count))

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Updated"})
        }
    except Exception as error:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": str(error)})
        }

if __name__ == "__main__":
    response = handler({}, None)
    print(response)
