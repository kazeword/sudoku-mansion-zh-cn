(() => {
  'use strict';
  const exact = new Map(__MAP__);;
  exact.set('Show solving hint', '查看解题提示');
  exact.set('Main Quest', '主线任务');
  exact.set('Mansion', '庄园');
  const attributes = ['title', 'aria-label', 'placeholder', 'alt'];

  function translatedCore(core) {
    if (exact.has(core)) return exact.get(core);
    let match;
    if ((match = core.match(/^Row (\d+) column (\d+)$/))) return `第 ${match[1]} 行，第 ${match[2]} 列`;
    if ((match = core.match(/^Removed (\d+) incorrect digits?$/))) return `已移除 ${match[1]} 个错误数字`;
    if ((match = core.match(/^There (?:is|are) (\d+) wrong digits?\.$/))) return `有 ${match[1]} 个错误数字。`;
    // 检查错误数字按钮：正文带 " in this room." 后缀，旧正则匹配不到
    if ((match = core.match(/^There (?:is|are) (\d+) wrong digits? in this room\.$/))) return `本房间有 ${match[1]} 个错误数字。`;
    if ((match = core.match(/^This room is fully filled but there (?:is|are) (\d+) wrong digits?\.$/))) return `本房间已填满，但有 ${match[1]} 个错误数字。`;
    if ((match = core.match(/^This room is fully filled but there (?:is|are) (\d+) wrong digits? in this room\.$/))) return `本房间已填满，但有 ${match[1]} 个错误数字。`;
    // 回退说明（Rewind 按钮旁的补充文字）
    if ((match = core.match(/^Rewinding undoes the last (\d+) moves?, removing (\d+) digits?\.$/))) return `回退将撤销最近 ${match[1]} 步，并移除 ${match[2]} 个数字。`;
    if ((match = core.match(/^Rewinding undoes the last (\d+) moves?\.$/))) return `回退将撤销最近 ${match[1]} 步。`;
    if (core === "They go further back than the undo history reaches, so this room can't be rewound past them.") return '它们超出了撤销历史的范围，本房间无法回退到那之前。';
    if ((match = core.match(/^Digit (\d+) entered into the boss cell$/))) return `数字 ${match[1]} 已填入首领格`;
    if ((match = core.match(/^Switch class \(currently (.+)\)$/))) return `切换身份（当前：${translatedCore(match[1])}）`;
    if ((match = core.match(/^(.+) class room$/))) return `${translatedCore(match[1])}身份房间`;
    return core;
  }

  function translateValue(value) {
    if (!value || !/[A-Za-z]/.test(value)) return value;
    const leading = value.match(/^\s*/)[0];
    const trailing = value.match(/\s*$/)[0];
    const core = value.slice(leading.length, value.length - trailing.length);
    const target = translatedCore(core);
    return target === core ? value : leading + target + trailing;
  }

  function translateElement(element) {
    for (const attribute of attributes) {
      if (!element.hasAttribute?.(attribute)) continue;
      const original = element.getAttribute(attribute);
      const target = translateValue(original);
      if (target !== original) element.setAttribute(attribute, target);
    }
  }

  function translateTree(root) {
    if (!root) return;
    if (root.nodeType === Node.TEXT_NODE) {
      const parent = root.parentElement;
      if (parent && !['SCRIPT', 'STYLE', 'NOSCRIPT'].includes(parent.tagName)) {
        const target = translateValue(root.nodeValue);
        if (target !== root.nodeValue) root.nodeValue = target;
      }
      return;
    }
    if (root.nodeType !== Node.ELEMENT_NODE && root.nodeType !== Node.DOCUMENT_NODE) return;
    if (root.nodeType === Node.ELEMENT_NODE) translateElement(root);
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    const nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    for (const node of nodes) translateTree(node);
    root.querySelectorAll?.('*').forEach(translateElement);
  }

  let queued = false;
  const pending = new Set();
  function queue(root) {
    pending.add(root);
    if (queued) return;
    queued = true;
    queueMicrotask(() => {
      queued = false;
      const roots = [...pending];
      pending.clear();
      roots.forEach(translateTree);
    });
  }

  const observer = new MutationObserver((mutations) => {
    for (const mutation of mutations) {
      if (mutation.type === 'childList') mutation.addedNodes.forEach(queue);
      else queue(mutation.target);
    }
  });

  document.documentElement.lang = 'zh-CN';
  translateTree(document);
  observer.observe(document.documentElement, {
    subtree: true,
    childList: true,
    characterData: true,
    attributes: true,
    attributeFilter: attributes,
  });
})();
