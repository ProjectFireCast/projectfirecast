module.exports = {
  entry: __dirname + "/src/app.js",
  output: {
    path:  __dirname + "/dist/pages/js",
    publicPath: "/pages/js/",
    filename: 'pages.var.js',
    library: 'WaveformPlaylist',
    libraryTarget: 'var'
  },
  devtool: "#source-map",
  module: {
    loaders: [{
      test: /\.js?$/,
      exclude: /node_modules/,
      loader: 'babel-loader'
    }]
  }
};