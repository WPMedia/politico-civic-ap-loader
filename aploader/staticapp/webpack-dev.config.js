const path = require('path');
const webpack = require('webpack');
const glob = require('glob');
const _ = require('lodash');

module.exports = port => ({
  resolve: {
    extensions: ['*', '.js', '.jsx', '.json'],
    alias: {
      adminTheme: path.resolve(__dirname, 'src/scss/theme'),
    }
  },
  entry: _.zipObject(
    glob.sync('./src/js/main-*.js*').map(f => path.basename(f, path.extname(f))),
    glob.sync('./src/js/main-*.js*').map(f => [
      `webpack-hot-middleware/client?path=http://localhost:${port}/__webpack_hmr&reload=true`,
      f,
    ]),
  ),
  output: {
    path: '/',
    filename: 'js/[name].js',
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: [
              [
                'env',
                {
                  targets: {
                    browsers: ['last 2 versions'],
                  },
                  debug: true,
                  modules: false,
                },
              ],
              'react',
              'stage-0',
              'airbnb',
            ],
            plugins: [
              'transform-class-properties',
            ]
          },
        },
      },
      {
        test: /\.s?css$/,
        use: [
          {
            loader: 'style-loader',
          },
          {
            loader: 'postcss-loader',
          },
          {
            loader: 'sass-loader',
          },
        ],
      },
    ],
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoEmitOnErrorsPlugin(),
  ],
  stats: 'minimal',
  devtool: 'cheap-module-eval-source-map',
  watch: true,
});
