from jkPyUtils.requests2.fetch import (
    get_url_binary,
    get_url_text,
)


binary, ext = get_url_binary('https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png')
filename = '%s%s' % ('downloaded', ext)
with open(filename, 'wb') as fw:
    fw.write(binary)
print('get_url_binary file saved: %s' % filename)

text = get_url_text('http://example.com/')
filename2 = 'index.html'
with open(filename2, 'w') as fw2:
    fw2.write(text)
print('get_url_text file saved: %s' % filename2)
