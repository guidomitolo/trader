import React from "react";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Line } from 'react-chartjs-2';
import cacheHistoryRequest from '../cache.js'

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const CoinChart = ({ coin, days }) => { 
  const datetimeOptions = { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit', second: '2-digit' }
  const [data, isLoading, currentPage, getData] = cacheHistoryRequest(
    `/api/history/${coin}/draw/${days}/`,
    []
  )
  if (!coin) {
    return <div>Please Select Coin</div>
  }
  if ((data && data.length > 0)) {
    let prices = data.map((item) => item.price)
    let market_caps = data.map((item) => item.market_cap)
    let total_volumes = data.map((item) => item.total_volume)
    let timestamps = data.map((item) => new Intl.DateTimeFormat('en-US', datetimeOptions).format(new Date(item.timestamp)))

    return <div>
      <DrawLineChart
          prices={prices}
          market_caps={market_caps}
          total_volumes={total_volumes}
          timestamps={timestamps}
      />
    </div>
  }
  return <div>No data</div>
};

export default CoinChart;


const DrawLineChart = ({prices, market_caps, total_volumes, timestamps}) => {

  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
      },
    },
  };

  const ChartDataPrice = {
    labels: timestamps,
    datasets: [
      {
        label: 'Price',
        data: prices,
        borderColor: 'rgb(255, 99, 132)',
        backgroundColor: 'rgba(255, 99, 132, 0.5)',
      },
    ],
  }

  const ChartDataVolume = {
    labels: timestamps,
    datasets: [
      {
        label: 'Total Volume',
        data: total_volumes,
        borderColor: 'rgb(39, 245, 46)',
        backgroundColor: 'rgba(39, 245, 46, 0.8)',
      },
    ],
  }

  const ChartDataMCap = {
    labels: timestamps,
    datasets: [
      {
        label: 'Market Cap',
        data: market_caps,
        borderColor: 'rgb(53, 162, 235)',
        backgroundColor: 'rgba(53, 162, 235, 0.5)',
      },
    ],
  }

  return <div>
    <div class="row">
      <Line options={options} data={ChartDataPrice} />
    </div>
    <div class="row">
      <div class="col-6">
        <Line options={options} data={ChartDataVolume} />
      </div>
      <div class="col-6">
        <Line options={options} data={ChartDataMCap} />
      </div>
    </div>
  </div>
}