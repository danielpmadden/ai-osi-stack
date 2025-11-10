import { HTMLAttributes } from 'react';
import { classNames } from '../utils/formatters';

export default function Panel({ className, ...props }: HTMLAttributes<HTMLDivElement>) {
  return <section className={classNames('gct-panel', className)} {...props} />;
}
