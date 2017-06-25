// import npm from "rollup-plugin-node-resolve";

// export default {
//   entry: "index-topojson.js",
//   format: "umd",
//   moduleName: "topojson",
//   plugins: [npm({jsnext: true})],
//   dest: "build/topojson.js"
// };

import ascii from "rollup-plugin-ascii";
import node from "rollup-plugin-node-resolve";

export default {
  entry: "index-topojson.js",
  format: "umd",
  moduleName: "topojson",
  plugins: [node(), ascii()],
//   plugins: [npm({jsnext: true})],
  dest: "build/topojson.js"
};