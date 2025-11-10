import { ButtonHTMLAttributes } from 'react';
import { classNames } from '../utils/formatters';

export default function Button({ className, ...props }: ButtonHTMLAttributes<HTMLButtonElement>) {
  return (
    <button
      className={classNames('gct-button', className)}
      {...props}
    />
  );
}
