import { existsSync } from 'fs';
import { statSync } from 'fs';
import { readFileSync } from 'fs';

var user_path = process.argv[2]

// if (existsSync('D:\\Documents'))
//   console.log('The path exists.');

export function checkPath(fpath) {
    try {
        if (existsSync(fpath)) {
            return true
        }
        else {
            return false
        }
    }
    catch (err) {
        return false
    }
}

export function checkDirectory(fpath) {
    if (checkPath(fpath)) {
      if (statSync(fpath).isDirectory()) {
        return true
      } else {
        return false
      }
    } else {
      return false
    }
  }

export function checkFile(fpath) {
    if (checkPath(fpath)) {
      if (statSync(fpath).isFile()) {
        return true
      } else {
        return false
      }
    } else {
      return false
    }
  }


export function readFile(fpath) {
    if (checkPath(fpath)) {
        if (checkFile(fpath)) {
            return readFileSync(fpath, {encoding: 'utf-8'});
        }
        else {
            return false
        }
    }
    else {
        return false
    }
}

console.log("Czy istnieje:", checkPath(user_path))
console.log("Czy katalog:", checkDirectory(user_path))
console.log("Czy plik:", checkFile(user_path))
console.log('Zawartość:', readFile(user_path))
