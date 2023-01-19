**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

*TODO:* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation
![get_all_svc_pod]:(./answer-img/get_all_svc_pods.png)

## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.
![grafana_web_ui]:(./answer-img/grafana_web_ui.png)
![data_source]:(./answer-img/data_source.png)

## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.
![prometheus_data_source]:(./answer-img/prometheus_data_source.png)

## Describe SLO/SLI
*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.

SLIs (Service Level Indicators) are metrics used to measure the performance of a service against its SLO (Service Level Objective). In this case, the SLIs would be the monthly uptime and request response time. Uptime would be measured as a percentage of time the service is available for use, and request response time would be measured as how quickly the service responds to requests from users.

## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 

1. Availability: This metric measures the percentage of time that a service is available to users. It can be measured by tracking the number of requests that are successfully completed and dividing it by the total number of requests made over a certain period of time.

2. Response Time: This metric measures how long it takes for a request to be processed and responded to. It can be measured by tracking the amount of time it takes for each request to be completed from start to finish.

3. Error Rate: This metric measures the percentage of requests that failed due to an error or other issue with the service. It can be measured by tracking the number of failed requests compared to the total number of requests made over a certain period of time.

4. Throughput: This metric measures how many requests can be processed in a given amount of time, such as per second or minute. It can be measured by tracking the number of successful requests completed over a certain period of time divided by that same period’s duration (seconds or minutes). 

5. Latency: This metric measures how long it takes for data to travel from one point in a system to another, such as from server to client or vice versa. It can be measured by tracking how long it takes for each request or response packet to travel between two points in a system over a certain period of time.

## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here. Also provide a (screenshot) sample Python file containing a trace and span code used to perform Jaeger traces on the backend service.

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue also include a screenshot of the tracer span to demonstrate how we can user a tracer to locate errors easily.

TROUBLE TICKET

Name:

Date:

Subject:

Affected Area:

Severity:

Description:


## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name four SLIs that you would use to measure the success of this SLO.

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create a list of 2-3 KPIs to accurately measure these metrics as well as a description of why those KPIs were chosen. We will make a dashboard for this, but first write them down here.

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  
