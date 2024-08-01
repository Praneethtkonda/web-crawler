from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class CrawlResponse(BaseModel):
    task_id: str = Field(..., title="Task ID", description="The unique identifier for this task.")
    sitemap_url: str = Field(..., title="Site Map URL", description="Download link to get the sitemap of the given URL")

class TaskInfo(BaseModel):
    task_id: str = Field(..., title="Task ID", description="The unique identifier for this task.")
    status: str = Field(..., title="Status",
        description="One of `PENDING`, `STARTED`, `RETRY`, `FAILURE`, `REVOKED`, or `SUCCESS`.")
    timestamp: Optional[str] = Field(None, title="Timestamp",
        description="The POSIX timestamp for when the task completed.")
    input_url: Optional[str] = Field(None, title="URL to be crawled", description="Input URL "
        "that needs to be crawled")
    sitemap_url: Optional[str] = Field(None, title="Signature URL", description="A presigned URL "
        "for downloading the sitemap")
    error_message: Optional[str] = Field(None, title="Error message",
        description="An error message if something went wrong.")


class SubmitCrawlingTask(BaseModel):
    url: Optional[str] = Field(None, title="URL to be crawled", description="A URL "
        "that will be crawled to build the site map")
    max_ttr: str = Field(..., title="Max time to run", description="Maximum time for the crawler to run")

class TaskStatus(str, Enum):
    STARTED = "STARTED"
    PENDING = "PENDING"
    RETRY = "RETRY"
    FAILURE = "FAILURE"
    REVOKED = "REVOKED"
    SUCCESS = "SUCCESS"

class TaskResult(BaseModel):
    state: Optional[str] = Field(None, title="Error message",
        description="One of `PENDING`, `STARTED`, `RETRY`, `FAILURE`, `REVOKED`, or `SUCCESS`.")
    sitemap_url: Optional[str] = Field(None, title="Signature URL", description="A presigned URL "
        "for downloading the sitemap")
    error_message: Optional[str] = Field(None, title="Error message",
        description="An error message if something went wrong.")
