const CopyWebpackPlugin = require("copy-webpack-plugin");

module.exports = {
  entry: {
    'd3-tip': './src/index.js',
    'examples/arrow-styles': './examples/arrow-styles.js',
    'examples/bars': './examples/bars.js',
    'examples/bulk-attr-style': './examples/bulk-attr-style.js',
    'examples/circles': './examples/circles.js',
    'examples/css-transitions': './examples/css-transitions.js',
    'examples/explicit-target': './examples/explicit-target.js',
    'examples/performance': './examples/performance.js'
  },
  output: {
    path: __dirname,
    filename: "./build/[name].js"
  },
  module: {
    loaders: [
      { test: /\.js$/, exclude: /node_modules/, loader: "babel" }
    ]
  },
  plugins: [
    new CopyWebpackPlugin([{
      from: './examples/*.{html,css}',
      to: './build'
    }])
  ]
};
