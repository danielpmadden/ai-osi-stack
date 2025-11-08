// SPDX-License-Identifier: Apache-2.0

import en from "./en.json";

type Messages = typeof en;
type MessageValue = string;

type Locale = "en";

const dictionaries: Record<Locale, Messages> = {
  en
};

const DEFAULT_LOCALE: Locale = "en";

type Interpolation = Record<string, string | number>;

const resolveMessage = (messages: Messages, key: string): MessageValue | undefined => {
  return key.split(".").reduce<MessageValue | Messages | undefined>((acc, segment) => {
    if (acc && typeof acc === "object" && segment in acc) {
      return acc[segment as keyof typeof acc] as MessageValue | Messages;
    }
    return undefined;
  }, messages) as MessageValue | undefined;
};

export const t = (key: string, interpolation: Interpolation = {}, locale: Locale = DEFAULT_LOCALE): string => {
  const messages = dictionaries[locale];
  const template = resolveMessage(messages, key) ?? key;

  return Object.entries(interpolation).reduce((result, [token, value]) => {
    const pattern = new RegExp(`\\{${token}\\}`, "g");
    return result.replace(pattern, String(value));
  }, template);
};
