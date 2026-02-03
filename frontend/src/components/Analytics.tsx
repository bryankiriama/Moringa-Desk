import { useState } from 'react';

const Analytics = () => {
  const [timeRange, setTimeRange] = useState('7d');
  
  const metrics = {
    '7d': {
      userGrowth: 12,
      questionGrowth: 8,
      answerGrowth: 15,
      engagement: 68
    },
    '30d': {
      userGrowth: 45,
      questionGrowth: 32,
      answerGrowth: 58,
      engagement: 72
    }
  };

  const chartData = {
    '7d': [20, 35, 45, 30, 55, 40, 65],
    '30d': [100, 120, 140, 110, 160, 130, 180]
  };

  const currentMetrics = metrics[timeRange as keyof typeof metrics];
  const currentChart = chartData[timeRange as keyof typeof chartData];

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h3 className="text-lg font-medium text-gray-900">Analytics & Reports</h3>
        <select
          value={timeRange}
          onChange={(e) => setTimeRange(e.target.value)}
          className="px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          <option value="7d">Last 7 days</option>
          <option value="30d">Last 30 days</option>
        </select>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div className="bg-white p-6 rounded-lg shadow">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-gray-600">User Growth</p>
              <p className="text-2xl font-semibold text-gray-900">+{currentMetrics.userGrowth}%</p>
            </div>
            <div className="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center">
              <span className="text-blue-600 text-sm">↗</span>
            </div>
          </div>
        </div>

        <div className="bg-white p-6 rounded-lg shadow">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-gray-600">Questions</p>
              <p className="text-2xl font-semibold text-gray-900">+{currentMetrics.questionGrowth}%</p>
            </div>
            <div className="w-8 h-8 bg-green-100 rounded-full flex items-center justify-center">
              <span className="text-green-600 text-sm">↗</span>
            </div>
          </div>
        </div>

        <div className="bg-white p-6 rounded-lg shadow">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-gray-600">Answers</p>
              <p className="text-2xl font-semibold text-gray-900">+{currentMetrics.answerGrowth}%</p>
            </div>
            <div className="w-8 h-8 bg-yellow-100 rounded-full flex items-center justify-center">
              <span className="text-yellow-600 text-sm">↗</span>
            </div>
          </div>
        </div>

        <div className="bg-white p-6 rounded-lg shadow">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-gray-600">Engagement</p>
              <p className="text-2xl font-semibold text-gray-900">{currentMetrics.engagement}%</p>
            </div>
            <div className="w-8 h-8 bg-purple-100 rounded-full flex items-center justify-center">
              <span className="text-purple-600 text-sm">●</span>
            </div>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="bg-white p-6 rounded-lg shadow">
          <h4 className="text-lg font-medium text-gray-900 mb-4">Activity Trend</h4>
          <div className="h-48 flex items-end space-x-2">
            {currentChart.map((value, index) => (
              <div key={index} className="flex-1 bg-blue-200 rounded-t" style={{ height: `${(value / Math.max(...currentChart)) * 100}%` }}>
                <div className="w-full bg-blue-500 rounded-t" style={{ height: '20%' }}></div>
              </div>
            ))}
          </div>
          <div className="flex justify-between mt-2 text-xs text-gray-500">
            <span>Mon</span>
            <span>Tue</span>
            <span>Wed</span>
            <span>Thu</span>
            <span>Fri</span>
            <span>Sat</span>
            <span>Sun</span>
          </div>
        </div>

        <div className="bg-white p-6 rounded-lg shadow">
          <h4 className="text-lg font-medium text-gray-900 mb-4">Top Categories</h4>
          <div className="space-y-4">
            <div className="flex items-center justify-between">
              <span className="text-sm text-gray-600">Technology</span>
              <div className="flex items-center space-x-2">
                <div className="w-24 bg-gray-200 rounded-full h-2">
                  <div className="bg-blue-500 h-2 rounded-full" style={{ width: '75%' }}></div>
                </div>
                <span className="text-sm text-gray-900">75%</span>
              </div>
            </div>
            <div className="flex items-center justify-between">
              <span className="text-sm text-gray-600">Science</span>
              <div className="flex items-center space-x-2">
                <div className="w-24 bg-gray-200 rounded-full h-2">
                  <div className="bg-green-500 h-2 rounded-full" style={{ width: '60%' }}></div>
                </div>
                <span className="text-sm text-gray-900">60%</span>
              </div>
            </div>
            <div className="flex items-center justify-between">
              <span className="text-sm text-gray-600">Business</span>
              <div className="flex items-center space-x-2">
                <div className="w-24 bg-gray-200 rounded-full h-2">
                  <div className="bg-yellow-500 h-2 rounded-full" style={{ width: '45%' }}></div>
                </div>
                <span className="text-sm text-gray-900">45%</span>
              </div>
            </div>
            <div className="flex items-center justify-between">
              <span className="text-sm text-gray-600">Education</span>
              <div className="flex items-center space-x-2">
                <div className="w-24 bg-gray-200 rounded-full h-2">
                  <div className="bg-purple-500 h-2 rounded-full" style={{ width: '30%' }}></div>
                </div>
                <span className="text-sm text-gray-900">30%</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="bg-white p-6 rounded-lg shadow">
        <h4 className="text-lg font-medium text-gray-900 mb-4">Recent Reports</h4>
        <div className="space-y-3">
          <div className="flex items-center justify-between p-3 bg-gray-50 rounded-md">
            <div>
              <p className="text-sm font-medium text-gray-900">User Activity Report</p>
              <p className="text-xs text-gray-500">Generated 2 hours ago</p>
            </div>
            <button className="text-blue-600 hover:text-blue-800 text-sm">Download</button>
          </div>
          <div className="flex items-center justify-between p-3 bg-gray-50 rounded-md">
            <div>
              <p className="text-sm font-medium text-gray-900">Content Analytics</p>
              <p className="text-xs text-gray-500">Generated yesterday</p>
            </div>
            <button className="text-blue-600 hover:text-blue-800 text-sm">Download</button>
          </div>
          <div className="flex items-center justify-between p-3 bg-gray-50 rounded-md">
            <div>
              <p className="text-sm font-medium text-gray-900">Performance Summary</p>
              <p className="text-xs text-gray-500">Generated 3 days ago</p>
            </div>
            <button className="text-blue-600 hover:text-blue-800 text-sm">Download</button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Analytics;