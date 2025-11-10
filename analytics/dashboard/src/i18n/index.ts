import dictionary from './en.json';

export function t(key: keyof typeof dictionary): string {
  return dictionary[key] ?? key;
}
