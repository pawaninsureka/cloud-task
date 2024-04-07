from google.cloud import tasks_v2


class BaseTaskClient:
    ...


class GoogleCloudTaskClient(BaseTaskClient):
    """Google cloud client class allows developers to manage the execution of
    background work in their applications.
    """

    @property
    def client(self) -> tasks_v2.CloudTasksClient():
        return tasks_v2.CloudTasksClient()
