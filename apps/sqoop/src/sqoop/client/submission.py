# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

from exception import SqoopException
from form import Form


class Submission(object):
  """
  Sqoop submission object.

  Example of sqoop submission dictionary received by server: {
    "progress": 0.0,
    "last-update-date": 1371775331096,
    "external-id": "job_201306201740_0001",
    "status": "RUNNING",
    "job": 1,
    "creation-date": 1371775311721,
    "external-link": "http://solaris:50030/jobdetails.jsp?jobid=job_201306201740_0001"
  }
  """
  def __init__(self, job_id, status, progress, created, updated, **kwargs):
    self.job_id = job_id
    self.status = status
    self.progress = progress
    self.created = created
    self.updated = updated
    self.external_id = kwargs.get('external_id', None)
    self.external_link = kwargs.get('external_link', None)

  @staticmethod
  def from_dict(submission_dict):
    submission_dict['job_id'] = submission_dict['job']
    submission_dict['created'] = submission_dict['creation-date']
    submission_dict['updated'] = submission_dict['last-update-date']
    submission_dict['external_id'] = submission_dict.get('external-id', None)
    submission_dict['external_link'] = submission_dict.get('external-link', None)
    return Submission(**submission_dict)

  def to_dict(self):
    d = {
      'job': self.job_id,
      'status': self.status,
      'progress': self.progress,
      'creation-date': self.created,
      'last-update-date': self.updated
    }

    if self.external_id:
      d['external-id'] = self.external_id

    if self.external_id:
      d['external-link'] = self.external_link

    return d


class SqoopSubmissionException(SqoopException):
  """
  Sqoop submission object.

  Example of sqoop submission exception dictionary received by server:
  {
    "all": [
      {
        "status": "FAILURE_ON_SUBMIT",
        "exception": "org.apache.hadoop.mapred.FileAlreadyExistsException: Output directory test already exists",
        "exception-trace": "org.apache.hadoop.mapred.FileAlreadyExistsException: Output directory test already exists\n\tat org.apache.hadoop.mapreduce.lib.output.FileOutputFormat.checkOutputSpecs(FileOutputFormat.java:132)\n\tat org.apache.hadoop.mapred.JobClient$2.run(JobClient.java:984)\n\tat org.apache.hadoop.mapred.JobClient$2.run(JobClient.java:945)\n\tat java.security.AccessController.doPrivileged(Native Method)\n\tat javax.security.auth.Subject.doAs(Subject.java:396)\n\tat org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1408)\n\tat org.apache.hadoop.mapred.JobClient.submitJobInternal(JobClient.java:945)\n\tat org.apache.hadoop.mapreduce.Job.submit(Job.java:566)\n\tat org.apache.sqoop.submission.mapreduce.MapreduceSubmissionEngine.submit(MapreduceSubmissionEngine.java:265)\n\tat org.apache.sqoop.framework.JobManager.submit(JobManager.java:382)\n\tat org.apache.sqoop.handler.SubmissionRequestHandler.submissionSubmit(SubmissionRequestHandler.java:128)\n\tat org.apache.sqoop.handler.SubmissionRequestHandler.handleActionEvent(SubmissionRequestHandler.java:106)\n\tat org.apache.sqoop.handler.SubmissionRequestHandler.handleEvent(SubmissionRequestHandler.java:72)\n\tat org.apache.sqoop.server.v1.SubmissionServlet.handlePostRequest(SubmissionServlet.java:44)\n\tat org.apache.sqoop.server.SqoopProtocolServlet.doPost(SqoopProtocolServlet.java:63)\n\tat javax.servlet.http.HttpServlet.service(HttpServlet.java:637)\n\tat javax.servlet.http.HttpServlet.service(HttpServlet.java:717)\n\tat org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:290)\n\tat org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:206)\n\tat org.apache.catalina.core.StandardWrapperValve.invoke(StandardWrapperValve.java:233)\n\tat org.apache.catalina.core.StandardContextValve.invoke(StandardContextValve.java:191)\n\tat org.apache.catalina.core.StandardHostValve.invoke(StandardHostValve.java:127)\n\tat org.apache.catalina.valves.ErrorReportValve.invoke(ErrorReportValve.java:103)\n\tat org.apache.catalina.core.StandardEngineValve.invoke(StandardEngineValve.java:109)\n\tat org.apache.catalina.connector.CoyoteAdapter.service(CoyoteAdapter.java:293)\n\tat org.apache.coyote.http11.Http11Processor.process(Http11Processor.java:861)\n\tat org.apache.coyote.http11.Http11Protocol$Http11ConnectionHandler.process(Http11Protocol.java:606)\n\tat org.apache.tomcat.util.net.JIoEndpoint$Worker.run(JIoEndpoint.java:489)\n\tat java.lang.Thread.run(Thread.java:662)\n",
        "job": 1,
        "creation-date": 1372390164970,
        "progress": -1.0,
        "last-update-date": 1372390164970
      }
    ]
  }
  """
  def __init__(self, job_id, status, progress, created, updated, **kwargs):
    self.job_id = job_id
    self.status = status
    self.progress = progress
    self.created = created
    self.updated = updated
    self.exception = kwargs.get('exception', None)
    self.exception_trace = kwargs.get('exception_trace', None)

  @staticmethod
  def from_dict(submission_dict):
    submission_dict['job_id'] = submission_dict['job']
    submission_dict['created'] = submission_dict['creation-date']
    submission_dict['updated'] = submission_dict['last-update-date']
    submission_dict['exception'] = submission_dict.get('exception', None)
    submission_dict['exception_trace'] = submission_dict.get('exception-trace', None)
    submission = SqoopSubmissionException(**submission_dict)
    return submission

  def to_dict(self):
    d = {
      'job': self.job_id,
      'status': self.status,
      'progress': self.progress,
      'creation-date': self.created,
      'last-update-date': self.updated
    }

    if self.exception:
      d['exception'] = self.exception

    if self.exception_trace:
      d['exception-trace'] = self.exception_trace

    return d