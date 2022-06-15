#!/usr/bin/env python3
from genericpath import isdir
import ntpath
import sys
from os import listdir, makedirs
from os.path import isfile, join
# import numpy

from pandas import DataFrame, read_csv
from matplotlib import pyplot

scenarios = sys.argv[1:]

axes = ()

for sc in scenarios:
  throughput_path = join(sc, 'throughput')
  latency_path = join(sc, 'latency')

  throughput_files = [join(throughput_path, f) for f in listdir(throughput_path) if isfile(join(throughput_path, f))]
  latency_files = [join(latency_path, f) for f in listdir(latency_path) if isfile(join(latency_path, f))]

  print(throughput_files, latency_files)

  result_data = DataFrame(columns=['avg_throughput', 'latency_90th'])

  for (throuput_file, latency_file) in zip(throughput_files, latency_files):
    throughput_series = read_csv(
      throuput_file,
      sep=' ',
      names=('unix_timestamp', 'req/s'),
      squeeze=True,
      index_col=0
    )

    latency_series = read_csv(
      latency_file,
      sep=' ',
      names=('unix_timestamp', 'latency'),
      squeeze=True,
      index_col=0
    )

    avg_throughput = throughput_series.mean()

    latency_90th = latency_series.quantile(0.9) / 1e6

    result_data = result_data.append(DataFrame([[avg_throughput, latency_90th]], columns=['avg_throughput', 'latency_90th']), ignore_index=True)

  # result_data = result_data.sort_values('avg_throughput')

  print(result_data)

  axes = (*axes, result_data['avg_throughput'], result_data['latency_90th'])

pyplot.ylim()
pyplot.xlabel("Vazão (média)")
pyplot.ylabel("Latência (percentil 90%)")
# pyplot.xticks(numpy.arange(min(axes[0]), max(axes[0]), 10.0))
# pyplot.yticks(numpy.arange(min(axes[0]), max(axes[0]), 10.0))
pyplot.plot(*axes)
head, tail = ntpath.split(sys.argv[1])
if not isdir(f"./figs/summary/{head}"): makedirs(f"./figs/summary/{head}")
pyplot.savefig(f"./figs/summary/{sys.argv[1]}.png")
pyplot.show()
