var path = require("path");

function resolve(filePath) {
  return path.join(__dirname, filePath);
}

module.exports = {
  devtool: "source-map",
  entry: {
    "bundle": ["babel-polyfill", resolve("./Main.fsproj")]
  },
  output: {
    filename: "[name].js",
    path: resolve("./public")
  },
  devServer: {
    contentBase: resolve("./public")
  },
  module: {
    rules: [
      {
        test: /\.fs(x|proj)?$/,
        use: {
          loader: "fable-loader"
        }
      },
      {
        test: /\.js$/,
        exclude: /node_modules[\\\/](?!fable-)/,
        use: {
          loader: "babel-loader"
        }
      }
    ]
  }
};
