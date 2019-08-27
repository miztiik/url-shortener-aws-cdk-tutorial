import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.aws_apigateway
import aws_cdk.aws_cloudwatch
import aws_cdk.aws_cloudwatch_actions
import aws_cdk.aws_dynamodb
import aws_cdk.aws_events
import aws_cdk.aws_events_targets
import aws_cdk.aws_lambda
import aws_cdk.aws_sns
import aws_cdk.aws_sns_subscriptions
import aws_cdk.core
__jsii_assembly__ = jsii.JSIIAssembly.load("cdk-watchful", "0.3.0", __name__, "cdk-watchful@0.3.0.jsii.tgz")
@jsii.interface(jsii_type="cdk-watchful.IWatchful")
class IWatchful(jsii.compat.Protocol):
    @staticmethod
    def __jsii_proxy_class__():
        return _IWatchfulProxy

    @jsii.member(jsii_name="addAlarm")
    def add_alarm(self, alarm: aws_cdk.aws_cloudwatch.Alarm) -> None:
        """
        :param alarm: -
        """
        ...

    @jsii.member(jsii_name="addSection")
    def add_section(self, title: str, *, links: typing.Optional[typing.List["QuickLink"]]=None) -> None:
        """
        :param title: -
        :param options: -
        :param links: -
        """
        ...

    @jsii.member(jsii_name="addWidgets")
    def add_widgets(self, *widgets: aws_cdk.aws_cloudwatch.IWidget) -> None:
        """
        :param widgets: -
        """
        ...


class _IWatchfulProxy():
    __jsii_type__ = "cdk-watchful.IWatchful"
    @jsii.member(jsii_name="addAlarm")
    def add_alarm(self, alarm: aws_cdk.aws_cloudwatch.Alarm) -> None:
        """
        :param alarm: -
        """
        return jsii.invoke(self, "addAlarm", [alarm])

    @jsii.member(jsii_name="addSection")
    def add_section(self, title: str, *, links: typing.Optional[typing.List["QuickLink"]]=None) -> None:
        """
        :param title: -
        :param options: -
        :param links: -
        """
        options = SectionOptions(links=links)

        return jsii.invoke(self, "addSection", [title, options])

    @jsii.member(jsii_name="addWidgets")
    def add_widgets(self, *widgets: aws_cdk.aws_cloudwatch.IWidget) -> None:
        """
        :param widgets: -
        """
        return jsii.invoke(self, "addWidgets", [*widgets])


@jsii.data_type(jsii_type="cdk-watchful.QuickLink", jsii_struct_bases=[], name_mapping={'title': 'title', 'url': 'url'})
class QuickLink():
    def __init__(self, *, title: str, url: str):
        """
        :param title: -
        :param url: -
        """
        self._values = {
            'title': title,
            'url': url,
        }

    @property
    def title(self) -> str:
        return self._values.get('title')

    @property
    def url(self) -> str:
        return self._values.get('url')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'QuickLink(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="cdk-watchful.SectionOptions", jsii_struct_bases=[], name_mapping={'links': 'links'})
class SectionOptions():
    def __init__(self, *, links: typing.Optional[typing.List["QuickLink"]]=None):
        """
        :param links: -
        """
        self._values = {
        }
        if links is not None: self._values["links"] = links

    @property
    def links(self) -> typing.Optional[typing.List["QuickLink"]]:
        return self._values.get('links')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'SectionOptions(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class WatchApiGateway(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="cdk-watchful.WatchApiGateway"):
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, rest_api: aws_cdk.aws_apigateway.RestApi, title: str, watchful: "IWatchful", cache_graph: typing.Optional[bool]=None, server_error_threshold: typing.Optional[jsii.Number]=None, watched_operations: typing.Optional[typing.List["WatchedOperation"]]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param rest_api: The API Gateway REST API that is being watched.
        :param title: The title of this section.
        :param watchful: The Watchful instance to add widgets into.
        :param cache_graph: Include a dashboard graph for caching metrics. Default: false
        :param server_error_threshold: Alarm when 5XX errors reach this threshold over 5 minutes. Default: 1 any 5xx HTTP response will trigger the alarm
        :param watched_operations: A list of operations to monitor separately. Default: - only API-level monitoring is added.
        """
        props = WatchApiGatewayProps(rest_api=rest_api, title=title, watchful=watchful, cache_graph=cache_graph, server_error_threshold=server_error_threshold, watched_operations=watched_operations)

        jsii.create(WatchApiGateway, self, [scope, id, props])


@jsii.data_type(jsii_type="cdk-watchful.WatchApiGatewayOptions", jsii_struct_bases=[], name_mapping={'cache_graph': 'cacheGraph', 'server_error_threshold': 'serverErrorThreshold', 'watched_operations': 'watchedOperations'})
class WatchApiGatewayOptions():
    def __init__(self, *, cache_graph: typing.Optional[bool]=None, server_error_threshold: typing.Optional[jsii.Number]=None, watched_operations: typing.Optional[typing.List["WatchedOperation"]]=None):
        """
        :param cache_graph: Include a dashboard graph for caching metrics. Default: false
        :param server_error_threshold: Alarm when 5XX errors reach this threshold over 5 minutes. Default: 1 any 5xx HTTP response will trigger the alarm
        :param watched_operations: A list of operations to monitor separately. Default: - only API-level monitoring is added.
        """
        self._values = {
        }
        if cache_graph is not None: self._values["cache_graph"] = cache_graph
        if server_error_threshold is not None: self._values["server_error_threshold"] = server_error_threshold
        if watched_operations is not None: self._values["watched_operations"] = watched_operations

    @property
    def cache_graph(self) -> typing.Optional[bool]:
        """Include a dashboard graph for caching metrics.

        default
        :default: false
        """
        return self._values.get('cache_graph')

    @property
    def server_error_threshold(self) -> typing.Optional[jsii.Number]:
        """Alarm when 5XX errors reach this threshold over 5 minutes.

        default
        :default: 1 any 5xx HTTP response will trigger the alarm
        """
        return self._values.get('server_error_threshold')

    @property
    def watched_operations(self) -> typing.Optional[typing.List["WatchedOperation"]]:
        """A list of operations to monitor separately.

        default
        :default: - only API-level monitoring is added.
        """
        return self._values.get('watched_operations')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'WatchApiGatewayOptions(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="cdk-watchful.WatchApiGatewayProps", jsii_struct_bases=[WatchApiGatewayOptions], name_mapping={'cache_graph': 'cacheGraph', 'server_error_threshold': 'serverErrorThreshold', 'watched_operations': 'watchedOperations', 'rest_api': 'restApi', 'title': 'title', 'watchful': 'watchful'})
class WatchApiGatewayProps(WatchApiGatewayOptions):
    def __init__(self, *, cache_graph: typing.Optional[bool]=None, server_error_threshold: typing.Optional[jsii.Number]=None, watched_operations: typing.Optional[typing.List["WatchedOperation"]]=None, rest_api: aws_cdk.aws_apigateway.RestApi, title: str, watchful: "IWatchful"):
        """
        :param cache_graph: Include a dashboard graph for caching metrics. Default: false
        :param server_error_threshold: Alarm when 5XX errors reach this threshold over 5 minutes. Default: 1 any 5xx HTTP response will trigger the alarm
        :param watched_operations: A list of operations to monitor separately. Default: - only API-level monitoring is added.
        :param rest_api: The API Gateway REST API that is being watched.
        :param title: The title of this section.
        :param watchful: The Watchful instance to add widgets into.
        """
        self._values = {
            'rest_api': rest_api,
            'title': title,
            'watchful': watchful,
        }
        if cache_graph is not None: self._values["cache_graph"] = cache_graph
        if server_error_threshold is not None: self._values["server_error_threshold"] = server_error_threshold
        if watched_operations is not None: self._values["watched_operations"] = watched_operations

    @property
    def cache_graph(self) -> typing.Optional[bool]:
        """Include a dashboard graph for caching metrics.

        default
        :default: false
        """
        return self._values.get('cache_graph')

    @property
    def server_error_threshold(self) -> typing.Optional[jsii.Number]:
        """Alarm when 5XX errors reach this threshold over 5 minutes.

        default
        :default: 1 any 5xx HTTP response will trigger the alarm
        """
        return self._values.get('server_error_threshold')

    @property
    def watched_operations(self) -> typing.Optional[typing.List["WatchedOperation"]]:
        """A list of operations to monitor separately.

        default
        :default: - only API-level monitoring is added.
        """
        return self._values.get('watched_operations')

    @property
    def rest_api(self) -> aws_cdk.aws_apigateway.RestApi:
        """The API Gateway REST API that is being watched."""
        return self._values.get('rest_api')

    @property
    def title(self) -> str:
        """The title of this section."""
        return self._values.get('title')

    @property
    def watchful(self) -> "IWatchful":
        """The Watchful instance to add widgets into."""
        return self._values.get('watchful')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'WatchApiGatewayProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class WatchDynamoTable(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="cdk-watchful.WatchDynamoTable"):
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, table: aws_cdk.aws_dynamodb.Table, title: str, watchful: "IWatchful", read_capacity_threshold_percent: typing.Optional[jsii.Number]=None, write_capacity_threshold_percent: typing.Optional[jsii.Number]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param table: -
        :param title: -
        :param watchful: -
        :param read_capacity_threshold_percent: Threshold for read capacity alarm (percentage). Default: 80
        :param write_capacity_threshold_percent: Threshold for read capacity alarm (percentage). Default: 80
        """
        props = WatchDynamoTableProps(table=table, title=title, watchful=watchful, read_capacity_threshold_percent=read_capacity_threshold_percent, write_capacity_threshold_percent=write_capacity_threshold_percent)

        jsii.create(WatchDynamoTable, self, [scope, id, props])


@jsii.data_type(jsii_type="cdk-watchful.WatchDynamoTableOptions", jsii_struct_bases=[], name_mapping={'read_capacity_threshold_percent': 'readCapacityThresholdPercent', 'write_capacity_threshold_percent': 'writeCapacityThresholdPercent'})
class WatchDynamoTableOptions():
    def __init__(self, *, read_capacity_threshold_percent: typing.Optional[jsii.Number]=None, write_capacity_threshold_percent: typing.Optional[jsii.Number]=None):
        """
        :param read_capacity_threshold_percent: Threshold for read capacity alarm (percentage). Default: 80
        :param write_capacity_threshold_percent: Threshold for read capacity alarm (percentage). Default: 80
        """
        self._values = {
        }
        if read_capacity_threshold_percent is not None: self._values["read_capacity_threshold_percent"] = read_capacity_threshold_percent
        if write_capacity_threshold_percent is not None: self._values["write_capacity_threshold_percent"] = write_capacity_threshold_percent

    @property
    def read_capacity_threshold_percent(self) -> typing.Optional[jsii.Number]:
        """Threshold for read capacity alarm (percentage).

        default
        :default: 80
        """
        return self._values.get('read_capacity_threshold_percent')

    @property
    def write_capacity_threshold_percent(self) -> typing.Optional[jsii.Number]:
        """Threshold for read capacity alarm (percentage).

        default
        :default: 80
        """
        return self._values.get('write_capacity_threshold_percent')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'WatchDynamoTableOptions(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="cdk-watchful.WatchDynamoTableProps", jsii_struct_bases=[WatchDynamoTableOptions], name_mapping={'read_capacity_threshold_percent': 'readCapacityThresholdPercent', 'write_capacity_threshold_percent': 'writeCapacityThresholdPercent', 'table': 'table', 'title': 'title', 'watchful': 'watchful'})
class WatchDynamoTableProps(WatchDynamoTableOptions):
    def __init__(self, *, read_capacity_threshold_percent: typing.Optional[jsii.Number]=None, write_capacity_threshold_percent: typing.Optional[jsii.Number]=None, table: aws_cdk.aws_dynamodb.Table, title: str, watchful: "IWatchful"):
        """
        :param read_capacity_threshold_percent: Threshold for read capacity alarm (percentage). Default: 80
        :param write_capacity_threshold_percent: Threshold for read capacity alarm (percentage). Default: 80
        :param table: -
        :param title: -
        :param watchful: -
        """
        self._values = {
            'table': table,
            'title': title,
            'watchful': watchful,
        }
        if read_capacity_threshold_percent is not None: self._values["read_capacity_threshold_percent"] = read_capacity_threshold_percent
        if write_capacity_threshold_percent is not None: self._values["write_capacity_threshold_percent"] = write_capacity_threshold_percent

    @property
    def read_capacity_threshold_percent(self) -> typing.Optional[jsii.Number]:
        """Threshold for read capacity alarm (percentage).

        default
        :default: 80
        """
        return self._values.get('read_capacity_threshold_percent')

    @property
    def write_capacity_threshold_percent(self) -> typing.Optional[jsii.Number]:
        """Threshold for read capacity alarm (percentage).

        default
        :default: 80
        """
        return self._values.get('write_capacity_threshold_percent')

    @property
    def table(self) -> aws_cdk.aws_dynamodb.Table:
        return self._values.get('table')

    @property
    def title(self) -> str:
        return self._values.get('title')

    @property
    def watchful(self) -> "IWatchful":
        return self._values.get('watchful')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'WatchDynamoTableProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class WatchLambdaFunction(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="cdk-watchful.WatchLambdaFunction"):
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, fn: aws_cdk.aws_lambda.Function, title: str, watchful: "IWatchful", duration_threshold_percent: typing.Optional[jsii.Number]=None, errors_per_minute_threshold: typing.Optional[jsii.Number]=None, throttles_per_minute_threshold: typing.Optional[jsii.Number]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param fn: -
        :param title: -
        :param watchful: -
        :param duration_threshold_percent: Threshold for the duration alarm as percentage of the function's timeout value. If this is set to 50%, the alarm will be set when p99 latency of the function exceeds 50% of the function's timeout setting. Default: 80
        :param errors_per_minute_threshold: Number of allowed errors per minute. If there are more errors than that, an alarm will trigger. Default: 0
        :param throttles_per_minute_threshold: Number of allowed throttles per minute. Default: 0
        """
        props = WatchLambdaFunctionProps(fn=fn, title=title, watchful=watchful, duration_threshold_percent=duration_threshold_percent, errors_per_minute_threshold=errors_per_minute_threshold, throttles_per_minute_threshold=throttles_per_minute_threshold)

        jsii.create(WatchLambdaFunction, self, [scope, id, props])


@jsii.data_type(jsii_type="cdk-watchful.WatchLambdaFunctionOptions", jsii_struct_bases=[], name_mapping={'duration_threshold_percent': 'durationThresholdPercent', 'errors_per_minute_threshold': 'errorsPerMinuteThreshold', 'throttles_per_minute_threshold': 'throttlesPerMinuteThreshold'})
class WatchLambdaFunctionOptions():
    def __init__(self, *, duration_threshold_percent: typing.Optional[jsii.Number]=None, errors_per_minute_threshold: typing.Optional[jsii.Number]=None, throttles_per_minute_threshold: typing.Optional[jsii.Number]=None):
        """
        :param duration_threshold_percent: Threshold for the duration alarm as percentage of the function's timeout value. If this is set to 50%, the alarm will be set when p99 latency of the function exceeds 50% of the function's timeout setting. Default: 80
        :param errors_per_minute_threshold: Number of allowed errors per minute. If there are more errors than that, an alarm will trigger. Default: 0
        :param throttles_per_minute_threshold: Number of allowed throttles per minute. Default: 0
        """
        self._values = {
        }
        if duration_threshold_percent is not None: self._values["duration_threshold_percent"] = duration_threshold_percent
        if errors_per_minute_threshold is not None: self._values["errors_per_minute_threshold"] = errors_per_minute_threshold
        if throttles_per_minute_threshold is not None: self._values["throttles_per_minute_threshold"] = throttles_per_minute_threshold

    @property
    def duration_threshold_percent(self) -> typing.Optional[jsii.Number]:
        """Threshold for the duration alarm as percentage of the function's timeout value.

        If this is set to 50%, the alarm will be set when p99 latency of the
        function exceeds 50% of the function's timeout setting.

        default
        :default: 80
        """
        return self._values.get('duration_threshold_percent')

    @property
    def errors_per_minute_threshold(self) -> typing.Optional[jsii.Number]:
        """Number of allowed errors per minute.

        If there are more errors than that, an alarm will trigger.

        default
        :default: 0
        """
        return self._values.get('errors_per_minute_threshold')

    @property
    def throttles_per_minute_threshold(self) -> typing.Optional[jsii.Number]:
        """Number of allowed throttles per minute.

        default
        :default: 0
        """
        return self._values.get('throttles_per_minute_threshold')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'WatchLambdaFunctionOptions(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="cdk-watchful.WatchLambdaFunctionProps", jsii_struct_bases=[WatchLambdaFunctionOptions], name_mapping={'duration_threshold_percent': 'durationThresholdPercent', 'errors_per_minute_threshold': 'errorsPerMinuteThreshold', 'throttles_per_minute_threshold': 'throttlesPerMinuteThreshold', 'fn': 'fn', 'title': 'title', 'watchful': 'watchful'})
class WatchLambdaFunctionProps(WatchLambdaFunctionOptions):
    def __init__(self, *, duration_threshold_percent: typing.Optional[jsii.Number]=None, errors_per_minute_threshold: typing.Optional[jsii.Number]=None, throttles_per_minute_threshold: typing.Optional[jsii.Number]=None, fn: aws_cdk.aws_lambda.Function, title: str, watchful: "IWatchful"):
        """
        :param duration_threshold_percent: Threshold for the duration alarm as percentage of the function's timeout value. If this is set to 50%, the alarm will be set when p99 latency of the function exceeds 50% of the function's timeout setting. Default: 80
        :param errors_per_minute_threshold: Number of allowed errors per minute. If there are more errors than that, an alarm will trigger. Default: 0
        :param throttles_per_minute_threshold: Number of allowed throttles per minute. Default: 0
        :param fn: -
        :param title: -
        :param watchful: -
        """
        self._values = {
            'fn': fn,
            'title': title,
            'watchful': watchful,
        }
        if duration_threshold_percent is not None: self._values["duration_threshold_percent"] = duration_threshold_percent
        if errors_per_minute_threshold is not None: self._values["errors_per_minute_threshold"] = errors_per_minute_threshold
        if throttles_per_minute_threshold is not None: self._values["throttles_per_minute_threshold"] = throttles_per_minute_threshold

    @property
    def duration_threshold_percent(self) -> typing.Optional[jsii.Number]:
        """Threshold for the duration alarm as percentage of the function's timeout value.

        If this is set to 50%, the alarm will be set when p99 latency of the
        function exceeds 50% of the function's timeout setting.

        default
        :default: 80
        """
        return self._values.get('duration_threshold_percent')

    @property
    def errors_per_minute_threshold(self) -> typing.Optional[jsii.Number]:
        """Number of allowed errors per minute.

        If there are more errors than that, an alarm will trigger.

        default
        :default: 0
        """
        return self._values.get('errors_per_minute_threshold')

    @property
    def throttles_per_minute_threshold(self) -> typing.Optional[jsii.Number]:
        """Number of allowed throttles per minute.

        default
        :default: 0
        """
        return self._values.get('throttles_per_minute_threshold')

    @property
    def fn(self) -> aws_cdk.aws_lambda.Function:
        return self._values.get('fn')

    @property
    def title(self) -> str:
        return self._values.get('title')

    @property
    def watchful(self) -> "IWatchful":
        return self._values.get('watchful')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'WatchLambdaFunctionProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="cdk-watchful.WatchedOperation", jsii_struct_bases=[], name_mapping={'http_method': 'httpMethod', 'resource_path': 'resourcePath'})
class WatchedOperation():
    def __init__(self, *, http_method: str, resource_path: str):
        """An operation (path and method) worth monitoring.

        :param http_method: The HTTP method for the operation (GET, POST, ...).
        :param resource_path: The REST API path for this operation (/, /resource/{id}, ...).
        """
        self._values = {
            'http_method': http_method,
            'resource_path': resource_path,
        }

    @property
    def http_method(self) -> str:
        """The HTTP method for the operation (GET, POST, ...)."""
        return self._values.get('http_method')

    @property
    def resource_path(self) -> str:
        """The REST API path for this operation (/, /resource/{id}, ...)."""
        return self._values.get('resource_path')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'WatchedOperation(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(IWatchful)
class Watchful(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="cdk-watchful.Watchful"):
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, alarm_email: typing.Optional[str]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param alarm_email: -
        """
        props = WatchfulProps(alarm_email=alarm_email)

        jsii.create(Watchful, self, [scope, id, props])

    @jsii.member(jsii_name="addAlarm")
    def add_alarm(self, alarm: aws_cdk.aws_cloudwatch.Alarm) -> None:
        """
        :param alarm: -
        """
        return jsii.invoke(self, "addAlarm", [alarm])

    @jsii.member(jsii_name="addSection")
    def add_section(self, title: str, *, links: typing.Optional[typing.List["QuickLink"]]=None) -> None:
        """
        :param title: -
        :param options: -
        :param links: -
        """
        options = SectionOptions(links=links)

        return jsii.invoke(self, "addSection", [title, options])

    @jsii.member(jsii_name="addWidgets")
    def add_widgets(self, *widgets: aws_cdk.aws_cloudwatch.IWidget) -> None:
        """
        :param widgets: -
        """
        return jsii.invoke(self, "addWidgets", [*widgets])

    @jsii.member(jsii_name="watchApiGateway")
    def watch_api_gateway(self, title: str, rest_api: aws_cdk.aws_apigateway.RestApi, *, cache_graph: typing.Optional[bool]=None, server_error_threshold: typing.Optional[jsii.Number]=None, watched_operations: typing.Optional[typing.List["WatchedOperation"]]=None) -> "WatchApiGateway":
        """
        :param title: -
        :param rest_api: -
        :param options: -
        :param cache_graph: Include a dashboard graph for caching metrics. Default: false
        :param server_error_threshold: Alarm when 5XX errors reach this threshold over 5 minutes. Default: 1 any 5xx HTTP response will trigger the alarm
        :param watched_operations: A list of operations to monitor separately. Default: - only API-level monitoring is added.
        """
        options = WatchApiGatewayOptions(cache_graph=cache_graph, server_error_threshold=server_error_threshold, watched_operations=watched_operations)

        return jsii.invoke(self, "watchApiGateway", [title, rest_api, options])

    @jsii.member(jsii_name="watchDynamoTable")
    def watch_dynamo_table(self, title: str, table: aws_cdk.aws_dynamodb.Table, *, read_capacity_threshold_percent: typing.Optional[jsii.Number]=None, write_capacity_threshold_percent: typing.Optional[jsii.Number]=None) -> "WatchDynamoTable":
        """
        :param title: -
        :param table: -
        :param options: -
        :param read_capacity_threshold_percent: Threshold for read capacity alarm (percentage). Default: 80
        :param write_capacity_threshold_percent: Threshold for read capacity alarm (percentage). Default: 80
        """
        options = WatchDynamoTableOptions(read_capacity_threshold_percent=read_capacity_threshold_percent, write_capacity_threshold_percent=write_capacity_threshold_percent)

        return jsii.invoke(self, "watchDynamoTable", [title, table, options])

    @jsii.member(jsii_name="watchLambdaFunction")
    def watch_lambda_function(self, title: str, fn: aws_cdk.aws_lambda.Function, *, duration_threshold_percent: typing.Optional[jsii.Number]=None, errors_per_minute_threshold: typing.Optional[jsii.Number]=None, throttles_per_minute_threshold: typing.Optional[jsii.Number]=None) -> "WatchLambdaFunction":
        """
        :param title: -
        :param fn: -
        :param options: -
        :param duration_threshold_percent: Threshold for the duration alarm as percentage of the function's timeout value. If this is set to 50%, the alarm will be set when p99 latency of the function exceeds 50% of the function's timeout setting. Default: 80
        :param errors_per_minute_threshold: Number of allowed errors per minute. If there are more errors than that, an alarm will trigger. Default: 0
        :param throttles_per_minute_threshold: Number of allowed throttles per minute. Default: 0
        """
        options = WatchLambdaFunctionOptions(duration_threshold_percent=duration_threshold_percent, errors_per_minute_threshold=errors_per_minute_threshold, throttles_per_minute_threshold=throttles_per_minute_threshold)

        return jsii.invoke(self, "watchLambdaFunction", [title, fn, options])

    @jsii.member(jsii_name="watchScope")
    def watch_scope(self, scope: aws_cdk.core.Construct, *, api_gateway: typing.Optional[bool]=None, dynamodb: typing.Optional[bool]=None, lambda_: typing.Optional[bool]=None) -> None:
        """
        :param scope: -
        :param options: -
        :param api_gateway: Automatically watch API Gateway APIs in the scope. Default: true
        :param dynamodb: Automatically watch all Amazon DynamoDB tables in the scope. Default: true
        :param lambda_: Automatically watch AWS Lambda functions in the scope. Default: true
        """
        options = WatchfulAspectProps(api_gateway=api_gateway, dynamodb=dynamodb, lambda_=lambda_)

        return jsii.invoke(self, "watchScope", [scope, options])


@jsii.implements(aws_cdk.core.IAspect)
class WatchfulAspect(metaclass=jsii.JSIIMeta, jsii_type="cdk-watchful.WatchfulAspect"):
    """A CDK aspect that can automatically watch all resources within a scope."""
    def __init__(self, watchful: "Watchful", *, api_gateway: typing.Optional[bool]=None, dynamodb: typing.Optional[bool]=None, lambda_: typing.Optional[bool]=None) -> None:
        """Defines a watchful aspect.

        :param watchful: The watchful to add those resources to.
        :param props: Options.
        :param api_gateway: Automatically watch API Gateway APIs in the scope. Default: true
        :param dynamodb: Automatically watch all Amazon DynamoDB tables in the scope. Default: true
        :param lambda_: Automatically watch AWS Lambda functions in the scope. Default: true
        """
        props = WatchfulAspectProps(api_gateway=api_gateway, dynamodb=dynamodb, lambda_=lambda_)

        jsii.create(WatchfulAspect, self, [watchful, props])

    @jsii.member(jsii_name="visit")
    def visit(self, node: aws_cdk.core.IConstruct) -> None:
        """All aspects can visit an IConstruct.

        :param node: -
        """
        return jsii.invoke(self, "visit", [node])


@jsii.data_type(jsii_type="cdk-watchful.WatchfulAspectProps", jsii_struct_bases=[], name_mapping={'api_gateway': 'apiGateway', 'dynamodb': 'dynamodb', 'lambda_': 'lambda'})
class WatchfulAspectProps():
    def __init__(self, *, api_gateway: typing.Optional[bool]=None, dynamodb: typing.Optional[bool]=None, lambda_: typing.Optional[bool]=None):
        """
        :param api_gateway: Automatically watch API Gateway APIs in the scope. Default: true
        :param dynamodb: Automatically watch all Amazon DynamoDB tables in the scope. Default: true
        :param lambda_: Automatically watch AWS Lambda functions in the scope. Default: true
        """
        self._values = {
        }
        if api_gateway is not None: self._values["api_gateway"] = api_gateway
        if dynamodb is not None: self._values["dynamodb"] = dynamodb
        if lambda_ is not None: self._values["lambda_"] = lambda_

    @property
    def api_gateway(self) -> typing.Optional[bool]:
        """Automatically watch API Gateway APIs in the scope.

        default
        :default: true
        """
        return self._values.get('api_gateway')

    @property
    def dynamodb(self) -> typing.Optional[bool]:
        """Automatically watch all Amazon DynamoDB tables in the scope.

        default
        :default: true
        """
        return self._values.get('dynamodb')

    @property
    def lambda_(self) -> typing.Optional[bool]:
        """Automatically watch AWS Lambda functions in the scope.

        default
        :default: true
        """
        return self._values.get('lambda_')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'WatchfulAspectProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="cdk-watchful.WatchfulProps", jsii_struct_bases=[], name_mapping={'alarm_email': 'alarmEmail'})
class WatchfulProps():
    def __init__(self, *, alarm_email: typing.Optional[str]=None):
        """
        :param alarm_email: -
        """
        self._values = {
        }
        if alarm_email is not None: self._values["alarm_email"] = alarm_email

    @property
    def alarm_email(self) -> typing.Optional[str]:
        return self._values.get('alarm_email')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'WatchfulProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["IWatchful", "QuickLink", "SectionOptions", "WatchApiGateway", "WatchApiGatewayOptions", "WatchApiGatewayProps", "WatchDynamoTable", "WatchDynamoTableOptions", "WatchDynamoTableProps", "WatchLambdaFunction", "WatchLambdaFunctionOptions", "WatchLambdaFunctionProps", "WatchedOperation", "Watchful", "WatchfulAspect", "WatchfulAspectProps", "WatchfulProps", "__jsii_assembly__"]

publication.publish()
