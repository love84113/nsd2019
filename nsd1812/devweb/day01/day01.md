# tedu_nsd1812_devweb_day01

http：超文本传输协议

html：超文本标记语言

## html基本格式

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>my html</title>
</head>
<body>

</body>
</html>
```

## 元素

也叫标签、标记。分为封闭型的双标记和单标记。

- 块级元素：不管数据量多少，至少占一整行，如标题元素h1-h6、p、div
- 行内元素：不会产生换行

## 大型网站建站

1. 规划网站功能
2. UI设计师设计版面
3. web前端设计师将设计出来的图片制作成网页
4. 后端程序员编写后台程序
5. 网站交给运维部发布到Web服务器



前端：html / css / js(javascript)

后端：python / php / java



## CSS：层叠样式表、级联样式表

### 分类

- 内联样式：类似于属性，在标签上直接设置样式
- 内部样式：在html的head标签中设置样式
- 外部样式：将样式表单独定义成一个文件

### 样式表的应用

注意的两个方面

- 选择器：给谁设置样式
- 样式声明：设置成什么样

### 样式表的特性

- 继承性：子元素的样式继承于父元素
- 层叠性：某一元素，它的样式可以有多个来源，不冲突时，效果累加
- 优先级：当多个样式应用在同一元素上，如果设置有冲突，样式有优先级

### 选择器

- 通用选择器：\* 匹配所有的选择器
- 元素选择器：针对html元素（标签）进行设置
- 类选择器：把需要具有相同样式的元素设置成一样的class，可以理解为分组
- id选择器：仅仅为某一个元素设置样式
- 群组选择器：如果需要对多个选择器设置相同的样式，可以用逗号将它们分开
- 伪类选择器：为超链接设置样式





