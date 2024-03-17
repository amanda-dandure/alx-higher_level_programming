#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let p = 0;
  while ((len - p) > 0) {
    const aux = list[len];
    list[len] = list[p];
    list[p] = aux;
    p++;
    len--;
  }
  return list;
};
