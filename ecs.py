import boto3

def get_next_count(count_order, current_count):
    try:
        index = count_order.index(str(current_count))
        next = count_order[index + 1]
    except:
        next = count_order[0]

    return next

def get_desired_count(cluster, service):
    ecs = boto3.client("ecs")
    description = ecs.describe_services(cluster=cluster, services=[service])
    services = description.get("services")

    if len(services) == 0:
        raise Exception("Service not found")

    desired_count = services[0].get("desiredCount")
    return desired_count

def set_desired_count(cluster, service, count):
    ecs = boto3.client("ecs")
    return ecs.update_service(cluster=cluster, service=service, desiredCount=count)
