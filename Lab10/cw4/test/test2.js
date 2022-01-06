import { strictEqual } from 'assert'; // import w stylu CommonJS
import { checkPath, checkDirectory, checkFile, readFile} from '../zad2.js';

describe('The checkPath() function', function () {
  it('Returns true for existing file', function () {
    strictEqual(checkPath('D:\\Documents\\Studia\\Skryptowe\\Repos\\Prog_skryptowe\\Lab10\\cw4\\test.txt'), true)
  });
  it('Returns true for existing directory', function () {
    strictEqual(checkPath('D:\\Documents\\Studia\\Skryptowe\\Repos\\Prog_skryptowe\\Lab10\\Zad1_1'), true)
  });
  it('Returns false for nonexistent dir/file', function () {
    strictEqual(checkPath('D:\\Documents\\Studia\\Skryptowe\\Repos\\Prog_skryptowe\\Lab10\\asfb'), false)
  });
});

describe('The checkDirectory() function', function () {
  it('Returns true for existing dir', function () {
    strictEqual(checkDirectory('D:\\Documents\\Studia\\Skryptowe\\Repos\\Prog_skryptowe\\Lab10\\Zad1_1'), true)
  });
  it('Returns false for existing file', function () {
    strictEqual(checkDirectory('D:\\Documents\\Studia\\Skryptowe\\Repos\\Prog_skryptowe\\Lab10\\cw4\\test.txt'), false)
  });
  it('Returns false for nonexistent dir/file', function () {
    strictEqual(checkDirectory('D:\\Documents\\Studia\\Skryptowe\\Repos\\Prog_skryptowe\\Lab10\\asfbss'), false)
  });
});

describe('The checkFile() function', function () {
  it('Returns true for existing file', function () {
    strictEqual(checkFile('D:\\Documents\\Studia\\Skryptowe\\Repos\\Prog_skryptowe\\Lab10\\cw4\\test.txt'), true)
  });
  it('Returns false for existing dir', function () {
    strictEqual(checkFile('D:\\Documents\\Studia\\Skryptowe\\Repos\\Prog_skryptowe\\Lab10\\Zad1_1'), false)
  });
  it('Returns false for nonexistent dir/file', function () {
    strictEqual(checkFile('D:\\Documents\\Studia\\Skryptowe\\Repos\\Prog_skryptowe\\Lab10\\asfbss'), false)
  });
});

describe('The readFile() function', function () {
  it('Returns file contents for existing file', function () {
    strictEqual(readFile('D:\\Documents\\Studia\\Skryptowe\\Repos\\Prog_skryptowe\\Lab10\\cw4\\test.txt'), 'testtesttest')
  });
  it('Returns false for existing dir', function () {
    strictEqual(readFile('D:\\Documents\\Studia\\Skryptowe\\Repos\\Prog_skryptowe\\Lab10\\Zad1_1'), false)
  });
  it('Returns null for nonexistent dir/file', function () {
    strictEqual(readFile('D:\\Documents\\Studia\\Skryptowe\\Repos\\Prog_skryptowe\\Lab10\\asfbss'), false)
  });
});