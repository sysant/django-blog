$(document).ready(function() {
    ClassicEditor
        .create(document.querySelector('#id_content'), {
            toolbar: {
                items: [
                    'heading', '|',
                    'blockQuote',
                    'bold', 'italic',
                    'fontColor', 'fontFamily', 'fontSize', 'fontBackgroundColor',
                    'highlight',
                    'link',
                    'bulletedList', 'numberedList', 'todoList',
                    '|',
                    'outdent', 'indent', '|',
                    'imageUpload', 'imageInsert', 'CKFinder',
                    'insertTable', 'mediaEmbed',
                    'code', 'codeBlock',
                    'horizontalLine', 'htmlEmbed',
                    'findAndReplace',
                    'superscript', 'subscript',
                    'sourceEditing',
                    '|',
                    'undo', 'redo'
                ]
            },
            language: 'zh-cn',
            image: {
                toolbar: [
                    'imageTextAlternative',
                    'imageStyle:inline',
                    'imageStyle:block',
                    'imageStyle:side'
                ]
            },
            ckfinder: {
                uploadUrl: '/upload/'
            },
            table: {
                contentToolbar: [
                    'tableColumn',
                    'tableRow',
                    'mergeTableCells'
                ]
            },
            licenseKey: '' // 保持空字符串即可
        })
        .then(editor => {
            window.editor = editor;
        })
        .catch(error => {
            console.error('CKEditor 初始化失败，错误信息：');
            console.error('Build ID: l0rtbv6zc870-j0z9q43obeqd');
            console.error(error.stack || error);
        });
});