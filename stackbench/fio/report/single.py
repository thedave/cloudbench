#coding:utf-8

def attribute_sum_factory(prop):
    """
    Returns a function that calculates an aggregate of a value across reads and writes
    """
    def fn(self):
        value = 0
        for mode, is_mode in [("read", self.job.is_read), ("write", self.job.is_write)]:
            if is_mode:
                value += int(self.report["{0}-{1}".format(mode, prop)])
        return value
    return fn


class SingleJobReport(object):
    """
    Process the output of a single job.
    """
    def __init__(self, job, report):
        """
        :param job: The Job this report was generated from
        :type job: stackbench.fio.config.job.Job
        :param report: A report generated by the engine
        :type report: dict
        """
        self.job = job
        self.report = report

    avg_iops = attribute_sum_factory("io-iops")
    avg_lat = attribute_sum_factory("latency-usec-total-avg")
    avg_bw = attribute_sum_factory("banwidth-avg")