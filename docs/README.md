# CS-Explorer应用更新说明

## ✨ **功能优化**

本次提交主要聚焦于提升应用的导航体验和整体布局优化。我们新增了一个**更新日志页面**，让用户可以轻松访问应用的最新动态和版本信息。同时，我们对侧边栏进行了更新，添加了指向**更新日志**的链接，使用户能够更直观地找到所需信息。

### 变更分类:
- `✨ **功能优化**`

### 关键代码展示:

```diff
--- a/src/App.jsx
+++ b/src/App.jsx
@@ -12,6 +12,7 @@ import FilesPage from './pages/Files';
 import UploadsPage from './pages/Uploads';
 import DownloadsPage from './pages/Downloads';
 import AboutPage from './pages/About';
+import ReleaseNotesPage from './pages/ReleaseNotes';
 
 function AppContent() {
   const [isSidebarCollapsed, setIsSidebarCollapsed] = useState(false);
@@ -76,7 +77,7 @@ function AppContent() {
           onClearNotifications={clearNotifications}
           onRemoveNotification={removeNotification}
         />
-        <main className="flex-1 p-6 overflow-auto">
+        <main className="relative flex-1 overflow-auto p-6">
           <Routes>
             <Route path="/" element={<Navigate to="/dashboard" replace />} />
             <Route path="/dashboard" element={<DashboardPage key={activeProfileId} />} />
@@ -85,6 +86,7 @@ function AppContent() {
             <Route path="/downloads" element={<DownloadsPage />} />
             <Route path="/settings" element={<SettingsPage onSettingsSaved={refreshState} />} />
             <Route path="/about" element={<AboutPage />} />
+            <Route path="/releasenotes" element={<ReleaseNotesPage />} />
           </Routes>
         </main>
       </LayoutBody>
--- a/src/components/sidebar.jsx
+++ b/src/components/sidebar.jsx
@@ -17,7 +17,8 @@ import {
   Folder,
   DownloadCloud,
   Info,
-  MessageSquare
+  MessageSquare,
+  ScrollText
 } from 'lucide-react'
 import { Link, useLocation } from 'react-router-dom'
 import { useTheme } from "./theme-provider"
@@ -39,6 +40,7 @@ export function Sidebar({ isCollapsed, onToggle }) {
     { id: 'downloads', href: '/downloads', icon: DownloadCloud, label: '下载管理' },
     { id: 'settings', href: '/settings', icon: Settings, label: '设置' },
     { id: 'about', href: '/about', icon: Info, label: '关于应用' },
+    { id: 'releasenotes', href: '/releasenotes', icon: ScrollText, label: '更新日志' },
   ]
 
   return (
--- a/src/pages/ReleaseNotes.jsx
+++ b/src/pages/ReleaseNotes.jsx
@@ -0,0 +1,17 @@
+import React from 'react';
+
+const ReleaseNotesPage = () => {
+  const releaseNotesUrl = "https://jiqingzhe2004.github.io/"; // 您可以在这里替换成您的更新日志网址
+
+  return (
+    <div className="absolute inset-0">
+      <iframe
+        src={releaseNotesUrl}
+        title="更新日志"
+        className="w-full h-full border-0"
+      />
+    </div>
+  );
+};
+
+export default ReleaseNotesPage; 
```
<!-- 57a9b91 at https://github.com/JiQingzhe2004/R2APP/commit/57a9b9191f00267ef459c933b0df1f421e7051a7 -->

---

## 📜 添加项目许可证

在本次提交中，我们为项目添加了必要的许可证文件（`LICENSE`），明确了项目的法律使用条款。这一举措不仅规范了项目的开源行为，也为使用者提供了清晰的权利和责任界定，是项目合规和透明化的重要一步。

`🆕 **新功能**`

许可证是开源项目不可或缺的一部分，它保护了项目的知识产权，同时也为使用者提供了明确的使用指导。通过添加许可证，我们确保了项目的合法性和透明度，为项目的长期发展和社区贡献奠定了坚实的基础。

由于添加的许可证内容较为标准，且主要涉及文本文件的创建，因此不包含核心逻辑的变更，故不展示关键代码。
<!-- 070eaa3 at https://github.com/JiQingzhe2004/R2APP/commit/070eaa3de84fa03b7245cb6f7707a1ff8d26d24c -->

---

## ✨ 功能优化

本次提交主要针对应用版本管理和用户界面进行了优化，提升了应用的透明度和用户体验。我们更新了 `.gitignore` 文件以排除日志和构建输出文件，优化了项目整洁度。同时，在 `package.json` 中修改了构建脚本以注入版本信息，并新增了 `inject-version.cjs` 脚本用于生成版本文件。最后，在 About 页面中显示了应用版本信息，并优化了用户界面，使用户能够更直观地了解应用版本和相关信息。

### 分类和图标
- `✨ **功能优化**`

### 关键代码展示

```diff
--- a/.gitignore
+++ b/.gitignore
@@ -2,4 +2,18 @@ node_modules
 .vscode
 out
 dist
-release
+release
+
+# Log files
+npm-debug.log*
+yarn-debug.log*
+yarn-error.log*
+
+# Build output
+dist-electron
+
+# icon
+resources/icon.ico
+
+# temp file
+src/version.json
--- a/package.json
+++ b/package.json
@@ -7,10 +7,11 @@
   "license": "MIT",
   "type": "module",
   "scripts": {
-    "dev": "electron-vite dev",
-    "build": "electron-vite build",
+    "dev": "node ./scripts/inject-version.cjs && electron-vite dev",
+    "build": "node ./scripts/inject-version.cjs && electron-vite build",
     "postinstall": "electron-builder install-app-deps",
-    "build:win": "npm run build && electron-builder --win --config",
+    "build:unpack": "npm run build && electron-builder --dir",
+    "build:win": "npm run build && electron-builder --win",
     "build:mac": "npm run build && electron-builder --mac --config",
     "build:linux": "npm run build && electron-builder --linux --config"
   },
--- a/scripts/inject-version.cjs
+++ b/scripts/inject-version.cjs
@@ -0,0 +1,18 @@
+const fs = require('fs');
+const path = require('path');
+
+// Get version from environment variable, or generate a dev version
+const version = process.env.VERSION || `dev-${new Date().toISOString()}`;
+
+const versionData = {
+  version: version,
+};
+
+// The path to write the version file to.
+// We write it inside `src` so it's easily importable by the frontend code.
+const outputPath = path.join(__dirname, '../src/version.json');
+
+// Write the version data to the file.
+fs.writeFileSync(outputPath, JSON.stringify(versionData, null, 2));
+
+console.log(`Version ${version} injected into ${outputPath}`);
--- a/src/pages/About.jsx
+++ b/src/pages/About.jsx
@@ -4,8 +4,11 @@ import WhiteLogo from '@/assets/WhiteLOGO.png'
 import BlackLogo from '@/assets/BlackLOGO.png'
 import { Github, GitCommit, UserCircle, Award, ArrowRight } from 'lucide-react'
 import { Button } from "@/components/ui/Button"
+import { useTheme } from '@/components/theme-provider';
+import versionData from '@/version.json';
 
 export default function AboutPage() {
+  const { theme } = useTheme();
   const [appInfo, setAppInfo] = useState({
     name: 'R2 存储管理器',
     version: '...',
@@ -26,8 +29,8 @@ export default function AboutPage() {
       <Card className="w-full max-w-2xl">
         <CardHeader className="text-center">
           <div className="flex justify-center mb-4">
-            <img src={BlackLogo} alt="Logo" className="h-20 w-20 hidden dark:block" />
-            <img src={WhiteLogo} alt="Logo" className="h-20 w-20 dark:hidden" />
+            <img src={BlackLogo} alt="App Logo" className="w-32 h-32 hidden dark:block" />
+            <img src={WhiteLogo} alt="App Logo" className="w-32 h-32 dark:hidden" />
           </div>
           <CardTitle className="text-3xl font-bold">{appInfo.name}</CardTitle>
         </CardHeader>
@@ -75,9 +78,24 @@ export default function AboutPage() {
           </div>
         </CardFooter>
       </Card>
-      <p className="text-xs text-muted-foreground">
-        Copyright © {new Date().getFullYear()} {appInfo.author}. All Rights Reserved.
-      </p>
+      <div className="text-center mt-6 text-xs text-muted-foreground space-y-2">
+         <div className="flex items-center justify-center gap-x-4">
+            <span>版本: {versionData.version}</span>
+            <div className="h-3 w-px bg-border" />
+            <a 
+              href={appInfo.githubUrl ? `${appInfo.githubUrl}/issues` : "#"}
+              target="_blank" 
+              rel="noopener noreferrer"
+              className="flex items-center gap-1 hover:text-primary transition-colors"
+            >
+              <Github size={12} />
+              <span>提交 Issue</span>
+            </a>
+        </div>
+        <p>
+          Copyright © {new Date().getFullYear()} {appInfo.author}. All Rights Reserved.
+        </p>
+      </div>
     </div>
   )
 }
```
<!-- 100329b at https://github.com/JiQingzhe2004/R2APP/commit/100329be787efa753a624b7c6ecb241f6d5c1e8b -->

---

## 🚀 v3.0.0

本次更新带来了令人兴奋的新功能和用户体验优化！我们不仅将版本号更新至 `v3.0.0`，还在文件预览组件中新增了复制代码到剪贴板的功能，极大地提升了用户在查看代码时的便捷性。同时，我们还引入了 `Copy` 图标，以增强界面的交互性和视觉吸引力。以下是本次更新的详细内容：

### 🆕 **新功能**

- **复制代码到剪贴板功能**：用户现在可以轻松地将文件内容复制到剪贴板，这对于需要分享代码片段或进行快速参考的用户来说，无疑是一个巨大的便利。
- **引入 `Copy` 图标**：我们添加了 `Copy` 图标，使其在文件预览组件中更加直观地指示复制功能，提升了界面的交互性和用户友好性。

### ✨ **功能优化**

- **用户体验优化**：通过新增复制代码到剪贴板的功能，我们优化了用户在查看代码时的体验，使其更加高效和便捷。

以下是本次更新的关键代码展示：

```diff
--- a/src/components/FilePreview.jsx
+++ b/src/components/FilePreview.jsx
@@ -9,7 +9,8 @@ import {
 import { Button } from './ui/Button';
 import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
 import { atomDark } from 'react-syntax-highlighter/dist/esm/styles/prism';
-import { Loader2 } from 'lucide-react';
+import { Loader2, Copy } from 'lucide-react';
+import { toast } from 'sonner';
 
 const isImage = (fileName = '') => {
   const imageExtensions = ['.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg'];
@@ -33,6 +34,13 @@ const FilePreview = ({ file, publicUrl, open, onOpenChange }) => {
 
   const fileName = file ? file.key.split('/').pop() : '';
 
+  const handleCopy = () => {
+    if (content) {
+      navigator.clipboard.writeText(content);
+      toast.success('代码已复制到剪贴板');
+    }
+  };
+
   useEffect(() => {
     if (open && file && isCode(fileName)) {
       const fetchContent = async () => {
@@ -92,9 +100,19 @@ const FilePreview = ({ file, publicUrl, open, onOpenChange }) => {
     
     if (isCode(fileName)) {
       return (
-        <SyntaxHighlighter language={fileName.split('.').pop()} style={atomDark} showLineNumbers>
-          {content}
-        </SyntaxHighlighter>
+        <div className="relative">
+          <Button
+            variant="ghost"
+            size="icon"
+            className="absolute top-2 right-2 h-7 w-7"
+            onClick={handleCopy}
+          >
+            <Copy className="h-4 w-4" />
+          </Button>
+          <SyntaxHighlighter language={fileName.split('.').pop()} style={atomDark} showLineNumbers>
+            {content}
+          </SyntaxHighlighter>
+        </div>
       );
     }
```
<!-- 1031df0 at https://github.com/JiQingzhe2004/R2APP/commit/1031df01689f39efdfa178fa0b5a117fdc303d35 -->

---

## 🚀 新增文件预览功能

本次提交为我们带来了令人兴奋的**新功能**——文件预览功能！现在，用户可以轻松预览代码和图片文件，极大地提升了用户体验。我们还在文件页面中集成了文件预览组件，使得操作更加便捷。

### 变更摘要

*   **🆕 新功能**: 我们引入了全新的文件预览功能，支持代码和图片文件的预览，让用户无需离开应用就能查看文件内容。
*   **🆕 新功能**: 在文件页面中集成了文件预览组件，优化了用户操作流程，提升了整体体验。
*   **✨ 功能优化**: 更新了依赖项，添加了`react-syntax-highlighter`库，以支持代码高亮显示，使代码预览更加美观和易读。

### 关键代码展示

```diff
--- a/electron/main/index.js
+++ b/electron/main/index.js
@@ -496,6 +496,48 @@ ipcMain.handle('create-folder', async (event, folderName) => {
   }
 });
 
+const PREVIEW_FILE_SIZE_LIMIT = 1024 * 1024; // 1MB
 
+ipcMain.handle('get-object-content', async (event, key) => {
+  const storage = await getStorageClient();
+  if (!storage) {
+    return { success: false, error: '未找到有效的存储配置' };
+  }
+  const { client, type, bucket } = storage;
+
+  try {
+    let content = '';
+    let fileTooLarge = false;
+
+    if (type === 'r2') {
+      const command = new GetObjectCommand({ Bucket: bucket, Key: key });
+      const response = await client.send(command);
+
+      if (response.ContentLength > PREVIEW_FILE_SIZE_LIMIT) {
+        fileTooLarge = true;
+      } else {
+        content = await response.Body.transformToString();
+      }
+    } else if (type === 'oss') {
+      const response = await client.get(key);
+      if (response.res.size > PREVIEW_FILE_SIZE_LIMIT) {
+        fileTooLarge = true;
+      } else {
+        content = response.content.toString('utf-8');
+      }
+    }
+
+    if (fileTooLarge) {
+      return { success: false, error: '文件过大，无法预览。' };
+    }
+
+    return { success: true, content };
+  } catch (error) {
+    console.error(`Failed to get content for ${key}:`, error);
+    return { success: false, error: `获取文件内容失败: ${error.message}` };
+  }
+});
+
 ipcMain.handle('get-downloads', (event) => {
   return store.get('downloads', []);
 });
--- a/electron/preload/index.mjs
+++ b/electron/preload/index.mjs
@@ -14,6 +14,7 @@ const api = {
   deleteObject: (key) => ipcRenderer.invoke('delete-object', key),
   deleteFolder: (prefix) => ipcRenderer.invoke('delete-folder', prefix),
   createFolder: (folderName) => ipcRenderer.invoke('create-folder', folderName),
+  getObjectContent: (key) => ipcRenderer.invoke('get-object-content', key),
   uploadFile: (filePath, key) => ipcRenderer.invoke('upload-file', { filePath, key }),
   showOpenDialog: () => ipcRenderer.invoke('show-open-dialog'),
   
--- a/package-lock.json
+++ b/package-lock.json
@@ -32,6 +32,7 @@
         "lucide-react": "^0.525.0",
         "proxy-agent": "^5.0.0",
         "react-router-dom": "^7.6.3",
+        "react-syntax-highlighter": "^15.6.1",
         "sonner": "^2.0.6",
         "uuid": "^11.1.0"
       },
@@ -1224,6 +1225,15 @@
         "@babel/core": "^7.0.0-0"
       }
     },
+    "node_modules/@babel/runtime": {
+      "version": "7.27.6",
+      "resolved": "https://registry.npmmirror.com/@babel/runtime/-/runtime-7.27.6.tgz",
+      "integrity": "sha512-vbavdySgbTTrmFE+EsiqUTzlOr5bzlnJtUv9PynGCAKvfQqjIXbvFdumPM/GxMDfyuGMJaJAU6TO4zc1Jf1i8Q==",
+      "license": "MIT",
+      "engines": {
+        "node": ">=6.9.0"
+      }
+    },
     "node_modules/@babel/template": {
       "version": "7.27.2",
       "resolved": "https://registry.npmmirror.com/@babel/template/-/template-7.27.2.tgz",
@@ -4800,6 +4810,15 @@
         "@types/node": "*"
       }
     },
+    "node_modules/@types/hast": {
+      "version": "2.3.10",
+      "resolved": "https://registry.npmmirror.com/@types/hast/-/hast-2.3.10.tgz",
+      "integrity": "sha512-McWspRw8xx8J9HurkVBfYj0xKoE25tOFlHGdx4MJ5xORQrMGZNqJhVQWaIbm6Oyla5kYOXtDiopzKRJzEOkwJw==",
+      "license": "MIT",
+      "dependencies": {
+        "@types/unist": "^2"
+      }
+    },
     "node_modules/@types/http-cache-semantics": {
       "version": "4.0.4",
       "resolved": "https://registry.npmmirror.com/@types/http-cache-semantics/-/http-cache-semantics-4.0.4.tgz",
@@ -4874,6 +4893,12 @@
         "@types/node": "*"
       }
     },
+    "node_modules/@types/unist": {
+      "version": "2.0.11",
+      "resolved": "https://registry.npmmirror.com/@types/unist/-/unist-2.0.11.tgz",
+      "integrity": "sha512-CmBKiL6NNo/OqgmMn95Fk9Whlp2mtvIv+KNpQKN2F4SjvrEesubTRWGYSg+BnWZOnlCaASTU1sMpsBOzgbYhnsA==",
+      "license": "MIT"
+    },
     "node_modules/@types/uuid": {
       "version": "9.0.8",
       "resolved": "https://registry.npmmirror.com/@types/uuid/-/uuid-9.0.8.tgz",
@@ -5857,6 +5882,36 @@
         "url": "https://github.com/chalk/chalk?sponsor=1"
       }
     },
+    "node_modules/character-entities": {
+      "version": "1.2.4",
+      "resolved": "https://registry.npmmirror.com/character-entities/-/character-entities-1.2.4.tgz",
+      "integrity": "sha512-iBMyeEHxfVnIakwOuDXpVkc54HijNgCyQB2w0VfGQThle6NXn50U6V/u+LDhxHcDUPojn6Kpga3PTAD8W1bQw==",
+      "license": "MIT",
+      "funding": {
+        "type": "github",
+        "url": "https://github.com/sponsors/wooorm"
+      }
+    },
+    "node_modules/character-entities-legacy": {
+      "version": "1.1.4",
+      "resolved": "https://registry.npmmirror.com/character-entities-legacy/-/character-entities-legacy-1.1.4.tgz",
+      "integrity": "sha512-3Xnr+7ZFS1uxeiUDvV02wQ+QDbc55o97tIV5zHScSPJpcLm/r0DFPcoY3tYRp+VZukxuMeKgXYmsXQHO05zQeA==",
+      "license": "MIT",
+      "funding": {
+        "type": "github",
+        "url": "https://github.com/sponsors/wooorm"
+      }
+    },
+    "node_modules/character-reference-invalid": {
+      "version": "1.1.4",
+      "resolved": "https://registry.npmmirror.com/character-reference-invalid/-/character-reference-invalid-1.1.4.tgz",
+      "integrity": "sha512-mKKUkUbhPpQlCOfIuZkvSEgktjPFIsZKRRbC6KWVEMvlzblj3i3asQv5ODsrwt0N3pHAEvjP8KTQPHkp0+6jOg==",
+      "license": "MIT",
+      "funding": {
+        "type": "github",
+        "url": "https://github.com/sponsors/wooorm"
+      }
+    },
```

通过这些关键代码的变更，我们成功实现了文件预览功能，并优化了用户体验。用户现在可以更方便地预览代码和图片文件，享受更流畅的操作体验。
<!-- 71f832c at https://github.com/JiQingzhe2004/R2APP/commit/71f832c295634a85e78416bb7113b82450071990 -->

---

## 🚀 新增文件夹管理功能

本次提交带来了对文件系统管理的重大升级，不仅支持了文件夹的创建与删除，还对文件列表显示和上传逻辑进行了深度优化。这些改进将极大地提升用户在管理大量文件时的效率和体验。

### 变更摘要

*   **🆕 新功能**: 引入了完整的文件夹管理功能，包括创建 (`create-folder`)、删除 (`delete-folder`) 文件夹的能力。
*   **✨ 功能优化**: 优化了文件列表显示，现在能够清晰地区分文件夹和文件，使用户更容易浏览和管理。
*   **✨ 功能优化**: 更新了文件上传逻辑，支持用户选择特定的文件夹作为上传目标，简化了批量上传的流程。
*   **✨ 功能优化**: 调整了文件删除逻辑，现在支持对文件夹的删除操作，同时确保了删除操作的完整性和安全性。
*   **✨ 功能优化**: 更新了依赖项，引入了 `@radix-ui/react-separator` 组件，以增强UI的分隔效果和整体美观度。

### 关键代码展示

```diff
+ipcMain.handle('delete-folder', async (event, prefix) => {
+  const storage = await getStorageClient();
+  if (!storage) {
+    return { success: false, error: '未找到有效的存储配置' };
+  }
+  const { client, type, bucket } = storage;
+
+  try {
+    let allKeys = [];
+    if (type === 'r2') {
+      let continuationToken;
+      do {
+        const response = await client.send(new ListObjectsV2Command({
+          Bucket: bucket,
+          Prefix: prefix,
+          ContinuationToken: continuationToken,
+        }));
+        if (response.Contents) {
+          allKeys.push(...response.Contents.map(item => item.Key));
+        }
+        continuationToken = response.NextContinuationToken;
+      } while (continuationToken);
+
+      if (allKeys.length > 0) {
+        // AWS S3 DeleteObjects can handle 1000 keys at a time
+        for (let i = 0; i < allKeys.length; i += 1000) {
+          const chunk = allKeys.slice(i, i + 1000);
+          await client.send(new DeleteObjectsCommand({
+            Bucket: bucket,
+            Delete: { Objects: chunk.map(k => ({ Key: k })) },
+          }));
+        }
+      }
+    } else if (type === 'oss') {
+      let continuationToken;
+      do {
+        const response = await client.list({
+          prefix: prefix,
+          marker: continuationToken,
+          'max-keys': 1000,
+        });
+        if (response.objects) {
+          allKeys.push(...response.objects.map(item => item.name));
+        }
+        continuationToken = response.nextMarker;
+      } while (continuationToken);
+
+      if (allKeys.length > 0) {
+        // OSS deleteMulti can handle 1000 keys at a time
+        await client.deleteMulti(allKeys, { quiet: true });
+      }
+    }
+
+    addRecentActivity('delete', `文件夹 "${prefix}" 已删除`, 'success');
+    return { success: true, deletedCount: allKeys.length };
+  } catch (error) {
+    console.error(`Failed to delete folder ${prefix}:`, error);
+    addRecentActivity('delete', `删除文件夹 "${prefix}" 失败`, 'error');
+    return { success: false, error: error.message };
+  }
+});
+
+ipcMain.handle('create-folder', async (event, folderName) => {
+  const storage = await getStorageClient();
+  if (!storage) {
+    return { success: false, error: '未找到有效的存储配置' };
+  }
+
+  const { client, type, bucket } = storage;
+
+  try {
+    if (type === 'r2') {
+      const { PutObjectCommand } = await import('@aws-sdk/client-s3');
+      await client.send(new PutObjectCommand({
+        Bucket: bucket,
+        Key: folderName,
+        Body: '',
+      }));
+    } else if (type === 'oss') {
+      await client.put(folderName, Buffer.from(''));
+    } else {
+      return { success: false, error: '不支持的存储类型' };
+    }
+    
+    addRecentActivity('create-folder', `文件夹 "${folderName}" 已创建`, 'success');
+    return { success: true };
+  } catch (error) {
+    console.error(`Failed to create folder ${folderName}:`, error);
+    addRecentActivity('create-folder', `创建文件夹 "${folderName}" 失败`, 'error');
+    return { success: false, error: error.message };
+  }
+});
```
<!-- ccb3eac at https://github.com/JiQingzhe2004/R2APP/commit/ccb3eac0c6a69e41794be4ea9f59056bc31051f5 -->

---

## 🚀 v2.0.1

本次更新带来了令人兴奋的新功能和改进，旨在提升用户体验和应用的实用性。以下是本次版本的主要变更：

`🆕 **新功能**`
- **新增最近活动记录功能**：现在，应用能够记录并展示用户的上传、下载和删除操作，让用户随时了解最近的文件活动。
- **仪表盘优化**：仪表盘现在会显示存储使用情况和最近活动，帮助用户更好地管理他们的文件和存储空间。
- **设置页面更新**：新增了对存储配额配置的支持，用户现在可以在设置页面中配置存储配额，进一步提升用户体验。

`✨ **功能优化**`
- **存储桶统计信息优化**：优化了获取存储桶统计信息的逻辑，现在会显示存储桶名称和存储配额，提供更详细的存储使用情况。
- **窗口状态管理优化**：增加了对窗口最大化状态变化的监听和处理，确保应用在窗口状态变化时能够正确更新状态。

以下是本次更新中最关键的代码变更：

```diff
--- a/electron/main/index.js
+++ b/electron/main/index.js
@@ -19,6 +19,21 @@ try {
 
 const store = new Store();
 
+const MAX_ACTIVITIES = 20;
+
+function addRecentActivity(type, message, status) {
+  const activities = store.get('recent-activities', []);
+  const newActivity = {
+    id: uuidv4(),
+    type,
+    message,
+    status,
+    timestamp: new Date().toISOString(),
+  };
+  const updatedActivities = [newActivity, ...activities].slice(0, MAX_ACTIVITIES);
+  store.set('recent-activities', updatedActivities);
+}
+
 // --- Data Migration ---
 function runMigration() {
   const oldSettings = store.get('settings');
@@ -82,6 +97,14 @@ function createWindow() {
     }
   })
 
+  mainWindow.on('maximize', () => {
+    mainWindow.webContents.send('window-maximized-status-changed', true)
+  })
+
+  mainWindow.on('unmaximize', () => {
+    mainWindow.webContents.send('window-maximized-status-changed', false)
+  })
+
   mainWindow.webContents.setWindowOpenHandler((details) => {
     shell.openExternal(details.url)
     return { action: 'deny' }
@@ -252,40 +275,47 @@ ipcMain.handle('check-status', async () => {
 ipcMain.handle('get-bucket-stats', async () => {
   const storage = await getStorageClient();
   if (!storage) {
-     return { success: false, error: '请先在设置中配置您的存储桶。' };
-   }
- 
-   let totalSize = 0;
-   let totalCount = 0;
-  let continuationToken;
-   
-   try {
+    return { success: false, error: '未找到活动的存储配置' };
+  }
+  const activeProfile = getActiveProfile();
+
+  try {
+    let totalCount = 0;
+    let totalSize = 0;
+    let continuationToken = undefined;
+
     if (storage.type === 'r2') {
-     do {
-          const command = new ListObjectsV2Command({ Bucket: storage.bucket, ContinuationToken: continuationToken });
-          const response = await storage.client.send(command);
-       if (response.Contents) {
-         totalCount += response.Contents.length;
-         totalSize += response.Contents.reduce((acc, obj) => acc + obj.Size, 0);
-       }
-          continuationToken = response.NextContinuationToken;
-        } while (continuationToken);
+      do {
+        const command = new ListObjectsV2Command({
+          Bucket: storage.bucket,
+          ContinuationToken: continuationToken,
+        });
+        const response = await storage.client.send(command);
+        totalCount += response.KeyCount || 0;
+        totalSize += response.Contents?.reduce((acc, obj) => acc + obj.Size, 0) || 0;
+        continuationToken = response.NextContinuationToken;
+      } while (continuationToken);
     } else if (storage.type === 'oss') {
-        let response;
-        do {
-            response = await storage.client.list({ marker: continuationToken, 'max-keys': 1000 });
-            if (response.objects) {
-                totalCount += response.objects.length;
-                totalSize += response.objects.reduce((acc, obj) => acc + obj.size, 0);
-            }
-            continuationToken = response.nextMarker;
-        } while (response.isTruncated);
+      do {
+        const response = await storage.client.list({ marker: continuationToken, 'max-keys': 1000 });
+        totalCount += response.objects?.length || 0;
+        totalSize += response.objects?.reduce((acc, obj) => acc + obj.size, 0) || 0;
+        continuationToken = response.nextMarker;
+      } while (continuationToken);
     }
-     return { success: true, data: { totalCount, totalSize } };
-   } catch (error) {
-     console.error('Failed to get bucket stats:', error);
-     return { success: false, error: '获取存储桶统计信息失败。' };
-   }
+    
+    const quota = parseInt(activeProfile?.storageQuotaGB, 10);
+
+    return { success: true, data: { 
+      totalCount, 
+      totalSize, 
+      bucketName: storage.bucket,
+      storageQuotaGB: !isNaN(quota) && quota > 0 ? quota : 10
+    } };
+  } catch (error) {
+    console.error('Failed to get bucket stats:', error);
+    return { success: false, error: error.message };
+  }
 });
 
 ipcMain.handle('list-objects', async (_, { continuationToken, prefix }) => {
@@ -328,19 +358,21 @@ ipcMain.handle('list-objects', async (_, { continuationToken, prefix }) => {
 ipcMain.handle('delete-object', async (_, key) => {
   const storage = await getStorageClient();
   if (!storage) {
-    return { success: false, error: '客户端未初始化。' };
+    return { success: false, error: '未找到活动的存储配置' };
   }
 
   try {
     if (storage.type === 'r2') {
-        const command = new DeleteObjectCommand({ Bucket: storage.bucket, Key: key });
-        await storage.client.send(command);
+      const command = new DeleteObjectCommand({ Bucket: storage.bucket, Key: key });
+      await storage.client.send(command);
     } else if (storage.type === 'oss') {
-        await storage.client.delete(key);
+      await storage.client.delete(key);
     }
+    addRecentActivity('delete', `删除了 ${key}`);
     return { success: true };
   } catch (error) {
-    return { success: false, error: `删除文件失败: ${error.message}` };
+    console.error(`Failed to delete object ${key}:`, error);
+    return { success: false, error: error.message };
   }
 });
 
@@ -472,6 +504,7 @@ ipcMain.on('download-file', async (event, key) => {
             store.set('download-tasks', finalTasks);
           }
           mainWindow.webContents.send('download-update', { type: 'progress', data: { id: taskId, progress: 100, status: 'completed' } });
+          addRecentActivity('download', `下载了 ${key}`);
           resolve();
         });
         writeStream.on('error', errorHandler);
@@ -561,4 +594,18 @@ ipcMain.handle('clear-completed-downloads', () => {
   if (mainWindow) {
     mainWindow.webContents.send('downloads-cleared', newTasks);
   }
+});
+
+ipcMain.handle('get-recent-activities', async () => {
+  try {
+    const activities = store.get('recent-activities', []);
+    return { success: true, data: activities };
+  } catch (error) {
+    console.error('Failed to get recent activities:', error);
+    return { success: false, error: error.message };
+  }
+});
+
+ipcMain.handle('is-window-maximized', () => {
+  return mainWindow?.isMaximized() || false;
 });
```
<!-- 48117cc at https://github.com/JiQingzhe2004/R2APP/commit/48117cc0f853359c74720768918932d9ac241033 -->

---

## 🚀 v2.0.1

本次更新带来了多项改进，旨在提升用户体验和应用稳定性。以下是本次版本的主要变更：

- **🆕 新功能**: 优化了头部组件的配置选择功能，新增了单选框，以提供更直观、便捷的用户选择体验。
- **✨ 功能优化**: 调整了文件页面的文件名显示方式，增加了截断效果，确保长文件名不会遮挡界面布局。同时，更新了关于页面的GitHub链接，指向最新的项目仓库。

### 关键代码展示

```diff
diff --git a/src/components/header.jsx b/src/components/header.jsx
index 10,7+10,9 @@ import {
   DropdownMenuItem,
   DropdownMenuTrigger,
   DropdownMenuSeparator,
-  DropdownMenuLabel
+  DropdownMenuLabel,
+  DropdownMenuRadioGroup,
+  DropdownMenuRadioItem,
 } from "@/components/ui/dropdown-menu"
 import { 
   Tooltip,
@@ -135,11+137,15 @@ export function Header({
               </Button>
             </DropdownMenuTrigger>
             <DropdownMenuContent className="w-[180px]">
-              {profiles.map(profile => (
-                <DropdownMenuItem key={profile.id} onSelect={() => onProfileSwitch(profile.id)} disabled={profile.id === activeProfileId}>
-                  {profile.name}
-                </DropdownMenuItem>
-              ))}
+              <DropdownMenuLabel>选择配置</DropdownMenuLabel>
+              <DropdownMenuSeparator />
+              <DropdownMenuRadioGroup value={activeProfileId} onValueChange={onProfileSwitch}>
+                {profiles.map(profile => (
+                  <DropdownMenuRadioItem key={profile.id} value={profile.id}>
+                    {profile.name}
+                  </DropdownMenuRadioItem>
+                ))}
+              </DropdownMenuRadioGroup>
             </DropdownMenuContent>
           </DropdownMenu>
         )}
diff --git a/src/components/ui/dropdown-menu.jsx b/src/components/ui/dropdown-menu.jsx
index 103,7+103,7 @@ const DropdownMenuRadioItem = React.forwardRef(({ className, children, ...props
     {...props}>
     <span className="absolute left-2 flex h-3.5 w-3.5 items-center justify-center">
       <DropdownMenuPrimitive.ItemIndicator>
-        <Circle className="h-2 w-2 fill-current" />
+        <Check className="h-4 w-4" />
       </DropdownMenuPrimitive.ItemIndicator>
     </span>
     {children}
diff --git a/src/pages/Files.jsx b/src/pages/Files.jsx
index 247,9+247,11 @@ export default function FilesPage({ isSearchOpen, onSearchOpenChange }) {
                     return (
                         <TableRow key={key} ref={isLastElement ? lastFileElementRef : null}>
                             <TableCell>{getFileIcon(file)}</TableCell>
-                            <TableCell className="font-medium">{key}</TableCell>
+                            <TableCell className="font-medium max-w-xs truncate" title={key}>
+                              {key}
+                            </TableCell>
                             <TableCell>{formatBytes(size)}</TableCell>
-                            <TableCell>{new Date(lastModified).toLocaleDateString()}</TableCell>
+                            <TableCell>{new Date(lastModified).toLocaleString()}</TableCell>
                             <TableCell className="text-right">
                                 <div className="flex items-center justify-end gap-2">
                                     {publicUrl && <Button variant="ghost" size="icon" onClick={() => handleCopyUrl(publicUrl)}><Copy className="h-4 w-4"/></Button>}
```
<!-- d3ac191 at https://github.com/JiQingzhe2004/R2APP/commit/d3ac1915e8beaf963eb4ce3df2e89345e945eafd -->

---

## ✨ 更新应用名称和版本

### 变更摘要
本次提交对应用进行了全面的更新，旨在提升用户体验和品牌形象。我们不仅**替换了应用名称和版本号**，还**优化了应用描述**，使其更准确地反映应用的新功能和目标用户。此外，我们还**更换了应用图标和LOGO**，以提升视觉吸引力，使应用在众多云存储管理工具中脱颖而出。

这些变更属于 `✨ **功能优化**` 类别，旨在为用户提供更清晰、更现代化的应用体验。

### 关键代码展示
```
\`\`\`diff
--- a/package.json
+++ b/package.json
@@ -1,7 +1,7 @@
 {
-  "name": "r2-explorer",
-  "version": "1.0.0",
-  "description": "一个用于管理Cloudflare R2存储的现代化桌面应用。",
+  "name": "CS-Explorer",
+  "version": "2.0.0",
+  "description": "一个用于管理在线云存储的现代化桌面应用。",
   "main": "out/main/index.js",
   "author": "吉庆喆",
   "license": "MIT",
\`\`\`
```
<!-- 8027d10 at https://github.com/JiQingzhe2004/R2APP/commit/8027d10dce10e71d206c7c772c34ffeb98ad8d3c -->

---

## 🚀 添加阿里云OSS支持

### 变更摘要

本次提交为应用程序引入了对阿里云OSS（对象存储服务）的全面支持，同时进行了关键的配置和逻辑重构，以适应多种存储类型的文件操作。这次更新不仅扩展了应用的存储能力，还优化了用户在设置页面中添加和管理OSS配置的体验。

- **🆕 新功能**: 引入阿里云OSS支持，允许用户通过OSS进行文件存储和检索。
- **✨ 功能优化**: 重构了文件处理逻辑，使其能够支持不同的存储类型（包括本地、R2和OSS），提升了应用的灵活性和可扩展性。
- **✨ 功能优化**: 优化了设置页面，增加了对OSS配置的添加和管理功能，改善了用户在配置存储服务时的体验。

### 关键代码展示

```diff
--- a/electron.vite.config.js
+++ b/electron.vite.config.js
@@ -9,7 +9,7 @@ export default defineConfig({
         input: {
           index: resolve(__dirname, 'electron/main/index.js')
         },
-        external: ['@electron-toolkit/utils', 'electron-store']
+        external: ['@electron-toolkit/utils', 'electron-store', 'ali-oss']
       }
     }
   },
--- a/electron/main/index.js
+++ b/electron/main/index.js
@@ -8,36 +8,7 @@ import fs from 'fs';
 import { v4 as uuidv4 } from 'uuid';
 import serve from 'electron-serve';
 import packageJson from '../../package.json' assert { type: 'json' };
-
-// Enhanced debugging - Print app paths
-console.log('App paths:');
-console.log('- App path:', app.getAppPath());
-console.log('- App directory structure:');
-try {
-  // Check if dist directory exists
-  const distPath = join(app.getAppPath(), 'dist');
-  console.log('- Dist path exists:', fs.existsSync(distPath));
-  if (fs.existsSync(distPath)) {
-    console.log('- Dist directory contents:', fs.readdirSync(distPath));
-    
-    // Check if index.html exists
-    const indexPath = join(distPath, 'index.html');
-    console.log('- index.html exists:', fs.existsSync(indexPath));
-  }
-} catch (err) {
-  console.error('Error checking directory structure:', err);
-}
-
-// Configure electron-serve with detailed logging
-const loadURL = serve({
-  directory: join(app.getAppPath(), 'dist'),
-  // Add a custom handler to log file requests
-  handler: (request, response) => {
-    const url = request.url.replace('app://', '');
-    console.log(`[electron-serve] Request for: ${url}`);
-    return null; // Let electron-serve handle the request normally
-  }
-});
+import OSS from 'ali-oss';
 
 // This is the correct way to disable sandbox for the entire app.
 app.commandLine.appendSwitch('no-sandbox');
@@ -51,26 +22,35 @@ const store = new Store();
 // --- Data Migration ---
 function runMigration() {
   const oldSettings = store.get('settings');
-  // Check if old structure exists and new structure doesn't
-  if (oldSettings && !store.has('profiles')) {
+  const oldProfiles = store.get('profiles');
+
+  // Check if old structure with base settings exists and new unified profiles don't
+  if (oldSettings && oldSettings.accountId && (!oldProfiles || oldProfiles.length === 0 || !oldProfiles[0].type)) {
     console.log('Migrating old settings to new profile structure...');
-    const newProfileId = uuidv4();
-    const newBaseSettings = {
+    
+    const migratedProfiles = (oldProfiles || []).map(p => ({
+      id: p.id || uuidv4(),
+      name: p.name || '默认R2配置',
+      bucketName: p.bucketName,
+      publicDomain: p.publicDomain || '',
+      // Add R2 specific fields from old base settings
+      type: 'r2',
       accountId: oldSettings.accountId,
       accessKeyId: oldSettings.accessKeyId,
       secretAccessKey: oldSettings.secretAccessKey,
-    };
-    const newProfile = {
-      id: newProfileId,
-      name: '默认配置',
-      bucketName: oldSettings.bucketName,
-      publicDomain: oldSettings.publicDomain || '',
-    };
+    }));
     
-    store.set('settings', newBaseSettings);
-    store.set('profiles', [newProfile]);
-    store.set('activeProfileId', newProfileId);
-    console.log('Migration complete.');
+    store.set('profiles', migratedProfiles);
+    
+    // If there was an active ID, keep it, otherwise set the first one as active.
+    if (!store.has('activeProfileId') && migratedProfiles.length > 0) {
+        store.set('activeProfileId', migratedProfiles[0].id);
+    }
+    
+    // Delete the old base settings key
+    store.delete('settings');
+    
+    console.log('Migration complete. Old base settings removed.');
   }
 }
 
@@ -80,7 +60,6 @@ runMigration();
 let mainWindow;
 
 function createWindow() {
-  console.log('Creating main window...');
   mainWindow = new BrowserWindow({
     width: 1200,
     height: 800,
@@ -92,51 +71,32 @@ function createWindow() {
       preload: join(__dirname, '../preload/index.mjs'),
       sandbox: false,
       contextIsolation: true,
-      // Enable dev tools in production for debugging
-      devTools: true
+      devTools: !app.isPackaged
     }
   })
 
   mainWindow.on('ready-to-show', () => {
-    console.log('Window ready to show');
     mainWindow.show()
-    // Open DevTools in production for debugging
-    if (!is.dev) {
-      mainWindow.webContents.openDevTools()
+    if (is.dev) {
+        mainWindow.webContents.openDevTools()
     }
   })
 
-  // Add error listener for failed page loads
-  mainWindow.webContents.on('did-fail-load', (event, errorCode, errorDescription, validatedURL) => {
-    console.error(`Failed to load URL: ${validatedURL}`);
-    console.error(`Error code: ${errorCode}, Description: ${errorDescription}`);
-  });
-
   mainWindow.webContents.setWindowOpenHandler((details) => {
     shell.openExternal(details.url)
     return { action: 'deny' }
   })
   
-  mainWindow.on('closed', () => {
-    console.log('Window closed');
-    mainWindow = null;
-  });
-
   if (is.dev && process.env['ELECTRON_RENDERER_URL']) {
-    console.log(`Loading dev URL: ${process.env['ELECTRON_RENDERER_URL']}`);
     mainWindow.loadURL(process.env['ELECTRON_RENDERER_URL'])
-    mainWindow.webContents.openDevTools()
   } else {
-    console.log('Loading production app via electron-serve');
-    loadURL(mainWindow)
+    mainWindow.loadFile(join(__dirname, '../../dist/index.html'))
   }
 }
 
 app.whenReady().then(() => {
-  console.log('App is ready');
   electronApp.setAppUserModelId('com.r2.explorer')
 
-  // Register F5 for refresh
   globalShortcut.register('F5', () => {
     const focusedWindow = BrowserWindow.getFocusedWindow();
     if (focusedWindow) {
@@ -152,7 +112,6 @@ app.whenReady().then(() => {
 })
 
 app.on('will-quit', () => {
-  // Unregister all shortcuts.
   globalShortcut.unregisterAll();
 });
 
@@ -163,150 +122,228 @@ app.on('window-all-closed', () => {
 })
 
 // IPC handlers
-function getActiveSettings() {
-  const baseSettings = store.get('settings', {});
+function getActiveProfile() {
   const profiles = store.get('profiles', []);
   const activeProfileId = store.get('activeProfileId');
   const activeProfile = profiles.find(p => p.id === activeProfileId);
 
   if (!activeProfile) {
+    console.error('No active profile found.');
     return null;
   }
 
-  return { ...baseSettings, ...activeProfile };
+  return activeProfile;
 }
 
 ipcMain.handle('get-settings', () => {
   return {
-    settings: store.get('settings', {}),
     profiles: store.get('profiles', []),
     activeProfileId: store.get('activeProfileId')
   }
 })
 
-ipcMain.handle('save-base-settings', (event, settings) => {
-    store.set('settings', settings)
-    return { success: true }
-})
-
 ipcMain.handle('save-profiles', (event, { profiles, activeProfileId }) => {
-  store.set('profiles', profiles);
-  store.set('activeProfileId', activeProfileId);
-  return { success: true };
+  try {
+    store.set('profiles', profiles);
+    store.set('activeProfileId', activeProfileId);
+    return { success: true };
+  } catch (error) {
+    console.error('Failed to save profiles:', error);
+    return { success: false, error: error.message };
+  }
 });
 
-ipcMain.handle('r2-test-connection', async (event, { settings, profile }) => {
-  const testSettings = { ...settings, ...profile };
-  if (!testSettings.accountId || !testSettings.accessKeyId || !testSettings.secretAccessKey || !testSettings.bucketName) {
-    return { success: false, error: '缺少必要的配置信息。' }
+ipcMain.handle('test-connection', async (event, profile) => {
+  if (profile.type === 'r2') {
+    if (!profile.accountId || !profile.accessKeyId || !profile.secretAccessKey || !profile.bucketName) {
+      return { success: false, error: '缺少 R2 配置信息。' }
+    }
+    const testS3Client = new S3Client({
+      region: 'auto',
+      endpoint: `https://${

... (diff内容过长，已截断)
```
<!-- 2f96d3b at https://github.com/JiQingzhe2004/R2APP/commit/2f96d3b346b3afdc4b1e3cb8b16314f763fccd8d -->

---

## 🚀 整合通知功能

本次提交全面整合了通知系统，为应用内消息管理引入了全新的上下文。通过在头部组件中嵌入通知显示与清除功能，并在文件、下载、上传及设置页面中集成反馈机制，我们显著提升了用户操作的即时性和便捷性。

### 🆕 **新功能**

*   **引入通知上下文**: 新增了 `NotificationProvider` 和相关钩子 `useNotifications`，为整个应用构建了统一的通知管理框架。
*   **头部组件增强**:  `Header` 组件现已支持显示未读通知计数、通知列表、批量标记已读、清除所有通知及移除单个通知功能。
*   **页面集成反馈**: 在文件、下载、上传和设置页面中，关键操作（如切换配置文件）现在会触发通知提示，使用户体验更加流畅。

#### 关键代码展示

```diff
--- a/src/App.jsx
+++ b/src/App.jsx
@@ -1,23 +1,25 @@
 import { useState, useEffect, useCallback } from 'react';
 import { ThemeProvider } from "@/components/theme-provider"
-import { Toaster } from 'sonner';
+import { Toaster, toast } from 'sonner';
 import { Layout, LayoutBody } from '@/components/ui/layout'
 import { Sidebar } from '@/components/sidebar'
 import { Header } from '@/components/header'
 import { HashRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
+import { NotificationProvider, useNotifications } from './contexts/NotificationContext';
 import DashboardPage from './pages/Dashboard';
 import SettingsPage from './pages/Settings';
 import FilesPage from './pages/Files';
 import UploadsPage from './pages/Uploads';
 import DownloadsPage from './pages/Downloads';
 import AboutPage from './pages/About';
 
-function App() {
+function AppContent() {
   const [isSidebarCollapsed, setIsSidebarCollapsed] = useState(false);
   const [isSearchDialogOpen, setIsSearchDialogOpen] = useState(false);
   const [r2Status, setR2Status] = useState({ loading: true, success: false, message: '正在检查连接...' });
   const [profiles, setProfiles] = useState([]);
   const [activeProfileId, setActiveProfileId] = useState(null);
+  const { notifications, unreadCount, addNotification, markAllAsRead, clearNotifications, removeNotification } = useNotifications();
 
   const checkStatus = useCallback(async () => {
     setR2Status({ loading: true, success: false, message: '正在检查连接...' });
@@ -47,40 +49,58 @@ function App() {
     const currentProfiles = await window.api.getSettings().then(d => d.profiles);
     await window.api.saveProfiles({ profiles: currentProfiles, activeProfileId: profileId });
     await refreshState();
+    const switchedProfile = currentProfiles.find(p => p.id === profileId);
+    if (switchedProfile) {
+        toast.success(`已切换到存储桶: ${switchedProfile.name}`);
+        addNotification({ message: `已切换到: ${switchedProfile.name}`, type: 'info' });
+    }
   };
 
   const toggleSidebar = () => {
     setIsSidebarCollapsed(prev => !prev);
   }
 
+  return (
+    <Router>
+      <Layout>
+        <Sidebar isCollapsed={isSidebarCollapsed} onToggle={toggleSidebar} />
+        <LayoutBody>
+          <Header 
+            onSearchClick={() => setIsSearchDialogOpen(true)} 
+            r2Status={r2Status}
+            profiles={profiles}
+            activeProfileId={activeProfileId}
+            onProfileSwitch={handleProfileSwitch}
+            notifications={notifications}
+            unreadCount={unreadCount}
+            onMarkAllRead={markAllAsRead}
+            onClearNotifications={clearNotifications}
+            onRemoveNotification={removeNotification}
+          />
+          <main className="flex-1 p-6 overflow-auto">
+            <Routes>
+              <Route path="/" element={<Navigate to="/dashboard" replace />} />
+              <Route path="/dashboard" element={<DashboardPage key={activeProfileId} />} />
+              <Route path="/files" element={<FilesPage key={activeProfileId} isSearchOpen={isSearchDialogOpen} onSearchOpenChange={setIsSearchDialogOpen} />} />
+              <Route path="/uploads" aname="uploads" element={<UploadsPage />} />
+              <Route path="/downloads" element={<DownloadsPage />} />
+              <Route path="/settings" element={<SettingsPage onSettingsSaved={refreshState} />} />
+              <Route path="/about" element={<AboutPage />} />
+            </Routes>
+          </main>
+        </LayoutBody>
+      </Layout>
+    </Router>
+  );
+}
+
+function App() {
   return (
     <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
       <Toaster richColors position="top-center" />
-      <Router>
-        <Layout>
-          <Sidebar isCollapsed={isSidebarCollapsed} onToggle={toggleSidebar} />
-          <LayoutBody>
-            <Header 
-              onSearchClick={() => setIsSearchDialogOpen(true)} 
-              r2Status={r2Status}
-              profiles={profiles}
-              activeProfileId={activeProfileId}
-              onProfileSwitch={handleProfileSwitch}
-            />
-            <main className="flex-1 p-6 overflow-auto">
-              <Routes>
-                <Route path="/" element={<Navigate to="/dashboard" replace />} />
-                <Route path="/dashboard" element={<DashboardPage key={activeProfileId} />} />
-                <Route path="/files" element={<FilesPage key={activeProfileId} isSearchOpen={isSearchDialogOpen} onSearchOpenChange={setIsSearchDialogOpen} />} />
-                <Route path="/uploads" aname="uploads" element={<UploadsPage />} />
-                <Route path="/downloads" element={<DownloadsPage />} />
-                <Route path="/settings" element={<SettingsPage onSettingsSaved={refreshState} />} />
-                <Route path="/about" element={<AboutPage />} />
-              </Routes>
-            </main>
-          </LayoutBody>
-        </Layout>
-      </Router>
+      <NotificationProvider>
+        <AppContent />
+      </NotificationProvider>
     </ThemeProvider>
   )
 }
--- a/src/components/header.jsx
+++ b/src/components/header.jsx
@@ -1,11 +1,16 @@
-import { Bell, TextSearch, ShieldEllipsis, ShieldCheck, ShieldX, ChevronsUpDown, Minus, Square, X } from 'lucide-react'
+import { useState, useEffect, useRef } from 'react';
+import { Bell, TextSearch, ShieldEllipsis, ShieldCheck, ShieldX, ChevronsUpDown, Minus, Square, X, CheckCircle, XCircle, Trash2, Info } from 'lucide-react'
 import { useLocation } from 'react-router-dom';
 import { Button } from '@/components/ui/Button';
+import { Card } from "@/components/ui/Card"
+import { Progress } from "@/components/ui/Progress"
 import { 
   DropdownMenu,
   DropdownMenuContent,
   DropdownMenuItem,
   DropdownMenuTrigger,
+  DropdownMenuSeparator,
+  DropdownMenuLabel
 } from "@/components/ui/dropdown-menu"
 import { 
   Tooltip,
@@ -14,9 +19,94 @@ import {
   TooltipTrigger,
 } from "@/components/ui/tooltip"
 
-export function Header({ onSearchClick, r2Status, profiles, activeProfileId, onProfileSwitch }) {
+function timeAgo(date) {
+  const seconds = Math.floor((new Date() - date) / 1000);
+  let interval = seconds / 31536000;
+  if (interval > 1) return Math.floor(interval) + " 年前";
+  interval = seconds / 2592000;
+  if (interval > 1) return Math.floor(interval) + " 个月前";
+  interval = seconds / 86400;
+  if (interval > 1) return Math.floor(interval) + " 天前";
+  interval = seconds / 3600;
+  if (interval > 1) return Math.floor(interval) + " 小时前";
+  interval = seconds / 60;
+  if (interval > 1) return Math.floor(interval) + " 分钟前";
+  return "刚刚";
+}
+
+const NotificationIcon = ({ type }) => {
+  switch (type) {
+    case 'success':
+      return <CheckCircle className="h-4 w-4 text-green-500" />;
+    case 'error':
+      return <XCircle className="h-4 w-4 text-red-500" />;
+    default:
+      return <Info className="h-4 w-4 text-blue-500" />;
+  }
+};
+
+export function Header({ 
+  onSearchClick, 
+  r2Status, 
+  profiles, 
+  activeProfileId, 
+  onProfileSwitch,
+  notifications,
+  unreadCount,
+  onMarkAllRead,
+  onClearNotifications,
+  onRemoveNotification
+}) {
   const location = useLocation();
   const showSearch = location.pathname === '/files';
+  const [activeNotification, setActiveNotification] = useState(null);
+  const [isPopupVisible, setIsPopupVisible] = useState(false);
+  const [progress, setProgress] = useState(100);
+  const prevNotificationsRef = useRef();
+
+  useEffect(() => {
+    if (notifications && (!prevNotificationsRef.current || notifications.length > prevNotificationsRef.current.length)) {
+      const newest = notifications[0];
+      if (newest && newest.id !== activeNotification?.id) {
+        setActiveNotification(newest);
+      }
+    }
+    prevNotificationsRef.current = notifications;
+  }, [notifications, acti
```
<!-- c89346c at https://github.com/JiQingzhe2004/R2APP/commit/c89346c844e2c23adc30595f95d76cfe26def236 -->

---

## 🛠️ 调整主窗口尺寸与新增应用图标

本次提交主要对应用程序的主窗口尺寸进行了调整，并新增了应用图标，旨在**增强界面的视觉效果**，提升用户体验。

### 变更摘要

在这次更新中，我们**调整了主窗口的尺寸**，将其从原有的 `900x670` 更改为 `1200x800`，以提供更宽敞的视觉空间，让用户在操作时拥有更好的体验。同时，我们还**为应用程序新增了图标**，特别是在Linux平台上，之前可能没有图标显示，现在通过指定图标路径 `../../resources/icon.ico`，使得应用在任务栏或 dock 中更加直观和美观。

这些改动属于**功能优化**的范畴，旨在通过提升界面的专业性和辨识度，让应用看起来更加完整和吸引人。

### 分类和图标

*   `✨ **功能优化**`

### 关键代码展示

```diff
--- a/electron/main/index.js
+++ b/electron/main/index.js
@@ -82,12 +82,12 @@ let mainWindow;
 function createWindow() {
   console.log('Creating main window...');
   mainWindow = new BrowserWindow({
-    width: 900,
-    height: 670,
+    width: 1200,
+    height: 800,
     show: false,
     autoHideMenuBar: true,
     frame: false,
-    ...(process.platform === 'linux' ? { icon: null } : {}),
+    ...(process.platform === 'linux' ? {} : { icon: join(__dirname, '../../resources/icon.ico') }),
     webPreferences: {
       preload: join(__dirname, '../preload/index.mjs'),
       sandbox: false,
```
<!-- 1a95b7b at https://github.com/JiQingzhe2004/R2APP/commit/1a95b7ba2bd850459ab94df32f6051e77315b700 -->

---

## 🛠️ 优化下载管理功能

本次提交主要针对下载管理功能进行了**重构**，提升了下载任务的状态管理能力，并增强了下载进度更新与错误处理机制。同时，更新了设置获取逻辑以支持活动配置文件，并清理了不再使用的预加载文件。

### 变更摘要

*   **🆕 新功能**: 下载任务状态管理重构，支持更细粒度的进度更新和错误反馈。
*   **✨ 功能优化**: 优化了下载进度计算逻辑，增加了下载速度显示，提升用户体验。
*   **🐞 Bug修复**: 修复了S3客户端初始化失败时的处理逻辑，避免了下载任务卡顿。

下载任务的状态管理现在更加灵活，能够实时反映下载进度和状态变化。此外，通过优化进度更新机制，用户可以更清晰地了解下载速度，从而更好地管理下载任务。

### 关键代码展示

```diff
@@ -388,86 +376,85 @@ ipcMain.on('r2-download-file', async (_, { key }) => {
     filePath,
     status: 'starting',
     progress: 0,
-    total: 0,
-    downloaded: 0,
-    createdAt: new Date().toISOString()
+    createdAt: new Date().toISOString(),
   };
-  
-  const currentTasks = store.get('downloads', {});
-  currentTasks[taskId] = task;
-  updateDownloads(currentTasks);
 
-  mainWindow.webContents.send('download-start', task);
-  
+  const tasks = store.get('download-tasks', {});
+  tasks[taskId] = task;
+  store.set('download-tasks', tasks);
+
+  mainWindow.webContents.send('download-update', { type: 'start', task });
+
   try {
     const command = new GetObjectCommand({ Bucket: bucketName, Key: key });
     const { Body, ContentLength } = await s3Client.send(command);
-    
-    if (!Body) throw new Error('无法获取文件内容。');
 
-    task.status = 'downloading';
-    task.total = ContentLength;
-    
-    const writeStream = fs.createWriteStream(filePath);
-    let lastProgressTime = Date.now();
+    if (!Body) {
+      throw new Error('Could not get file body from S3');
+    }
+
+    const fileStream = fs.createWriteStream(filePath);
+    let downloaded = 0;
+    let lastProgressTime = 0;
     let lastDownloaded = 0;
 
     Body.on('data', (chunk) => {
-      task.downloaded += chunk.length;
-      if (task.total > 0) {
-        task.progress = Math.round((task.downloaded / task.total) * 100);
-      }
+      downloaded += chunk.length;
+      const progress = ContentLength ? Math.round((downloaded / ContentLength) * 100) : 0;
       
       const now = Date.now();
-      const timeDiff = (now - lastProgressTime) / 1000;
-      if (timeDiff > 0.5) {
-        const bytesDiff = task.downloaded - lastDownloaded;
-        const speed = timeDiff > 0 ? bytesDiff / timeDiff : 0;
-        lastDownloaded = task.downloaded;
+      let speed = 0;
+      if (now - lastProgressTime > 500) { // Update speed every 500ms
+        const timeDiff = (now - lastProgressTime) / 1000;
+        const bytesDiff = downloaded - lastDownloaded;
+        speed = timeDiff > 0 ? bytesDiff / timeDiff : 0;
         lastProgressTime = now;
-        
-        const tasks = store.get('downloads', {});
-        tasks[taskId] = { ...tasks[taskId], ...task, speed };
-        updateDownloads(tasks);
-        mainWindow.webContents.send('download-progress', { id: taskId, progress: task.progress, speed: speed, status: 'downloading' });
+        lastDownloaded = downloaded;
+      }
+      
+      const currentTasks = store.get('download-tasks', {});
+      if (currentTasks[taskId]) {
+        currentTasks[taskId] = { ...currentTasks[taskId], progress, status: 'downloading', speed };
+        store.set('download-tasks', currentTasks);
       }
+      mainWindow.webContents.send('download-update', { type: 'progress', data: { id: taskId, progress, speed, status: 'downloading' } });
     });
 
-    Body.pipe(writeStream);
-
+    Body.pipe(fileStream);
+    
     await new Promise((resolve, reject) => {
-      writeStream.on('finish', () => {
-        task.status = 'completed';
-        task.progress = 100;
-        
-        const tasks = store.get('downloads', {});
-        tasks[taskId] = { ...tasks[taskId], ...task, speed: 0 };
-        updateDownloads(tasks);
-        mainWindow.webContents.send('download-progress', { id: taskId, progress: 100, status: 'completed' });
+      fileStream.on('finish', () => {
+        const finalTasks = store.get('download-tasks', {});
+        if (finalTasks[taskId]) {
+          finalTasks[taskId].status = 'completed';
+          finalTasks[taskId].progress = 100;
+          finalTasks[taskId].speed = 0;
+          store.set('download-tasks', finalTasks);
+        }
+        mainWindow.webContents.send('download-update', { type: 'progress', data: { id: taskId, progress: 100, status: 'completed' } });
         resolve();
       });
       const errorHandler = (err) => {
-         task.status = 'error';
-         task.error = err.message;
-
-         const tasks = store.get('downloads', {});
-         tasks[taskId] = { ...tasks[taskId], ...task };
-         updateDownloads(tasks);
-         mainWindow.webContents.send('download-progress', { id: taskId, status: 'error', error: err.message });
-         reject(err);
-      }
-      writeStream.on('error', errorHandler);
+        const errorTasks = store.get('download-tasks', {});
+        if (errorTasks[taskId]) {
+          errorTasks[taskId].status = 'error';
+          errorTasks[taskId].error = err.message;
+          store.set('download-tasks', errorTasks);
+        }
+        mainWindow.webContents.send('download-update', { type: 'progress', data: { id: taskId, status: 'error', error: err.message } });
+        reject(err);
+      };
+      fileStream.on('error', errorHandler);
       Body.on('error', errorHandler);
     });
-
   } catch (error) {
-    task.status = 'error';
-    task.error = error.message;
-
-    const tasks = store.get('downloads', {});
-    tasks[taskId] = task;
-    updateDownloads(tasks);
-    mainWindow.webContents.send('download-progress', { id: taskId, status: 'error', error: error.message });
+    const errorTasks = store.get('download-tasks', {});
+    if (errorTasks[taskId]) {
+      errorTasks[taskId].status = 'error';
+      errorTasks[taskId].error = error.message;
+      store.set('download-tasks', errorTasks);
+    }
+    mainWindow.webContents.send('download-update', { type: 'progress', data: { id: taskId, status: 'error', error: error.message } });
   }
 });
```
<!-- 23c5f93 at https://github.com/JiQingzhe2004/R2APP/commit/23c5f9352c9e4caea7b8dfc2ab487e7b1c75c45e -->

---

## 🚀 更新依赖项与新增应用信息功能

本次提交主要包含以下核心变更：

*   **依赖项更新**: 升级了 `lucide-react` 至 `0.525.0` 版本，以获取最新的图标组件和潜在的性能改进。
*   **新增应用信息获取功能**: 在主进程 (`electron/main/index.js`) 中添加了 `get-app-info` IPC 处理函数，用于获取应用的关键信息，包括：
    *   应用名称 (`app.getName()`)
    *   应用版本 (`app.getVersion()`)
    *   作者 (`packageJson.author`)
    *   描述 (`packageJson.description`)
    *   许可证 (`packageJson.license`)
*   **新增关于页面**: 在应用中添加了 `/about` 路由和对应的 `AboutPage` 组件，用于展示应用的详细信息，包括名称、版本、作者、描述、许可证，并提供了 GitHub 链接入口。
*   **UI 组件更新**: 更新了 `src/components/header.jsx` 和 `src/components/sidebar.jsx` 中的 Lucide React 图标，以反映 `lucide-react` 的版本更新，并调整了侧边栏导航项，将“关于应用” (`Info` 图标) 作为导航项添加到侧边栏中。

这些变更共同提升了应用的**用户体验**和**可维护性**，同时为用户提供了更便捷地了解应用信息的方式。

```diff
--- a/electron/main/index.js
+++ b/electron/main/index.js
@@ -7,6 +7,7 @@ import { Upload } from "@aws-sdk/lib-storage";
 import fs from 'fs';
 import { v4 as uuidv4 } from 'uuid';
 import serve from 'electron-serve';
+import packageJson from '../../package.json' assert { type: 'json' };
 
 // Enhanced debugging - Print app paths
 console.log('App paths:');
@@ -555,4 +556,14 @@ ipcMain.on('maximize-window', () => {
 
 ipcMain.on('close-window', () => {
   mainWindow?.close();
+});
+
+ipcMain.handle('get-app-info', () => {
+  return {
+    name: app.getName(),
+    version: app.getVersion(),
+    author: packageJson.author,
+    description: packageJson.description,
+    license: packageJson.license,
+  };
 });
--- a/electron/preload/index.mjs
+++ b/electron/preload/index.mjs
@@ -61,6 +61,7 @@ const api = {
   minimizeWindow: () => ipcRenderer.send('minimize-window'),
   maximizeWindow: () => ipcRenderer.send('maximize-window'),
   closeWindow: () => ipcRenderer.send('close-window'),
+  getAppInfo: () => ipcRenderer.invoke('get-app-info'),
 }
 
 // Use `contextBridge` APIs to expose Electron APIs to
--- a/src/App.jsx
+++ b/src/App.jsx
@@ -10,6 +10,7 @@ import SettingsPage from './pages/Settings';
 import FilesPage from './pages/Files';
 import UploadsPage from './pages/Uploads';
 import DownloadsPage from './pages/Downloads';
+import AboutPage from './pages/About';
 
 function App() {
   const [isSidebarCollapsed, setIsSidebarCollapsed] = useState(false);
@@ -74,6 +75,7 @@ function App() {
                 <Route path="/uploads" aname="uploads" element={<UploadsPage />} />
                 <Route path="/downloads" element={<DownloadsPage />} />
                 <Route path="/settings" element={<SettingsPage onSettingsSaved={refreshState} />} />
+                <Route path="/about" element={<AboutPage />} />
               </Routes>
             </main>
           </LayoutBody>
--- a/src/components/header.jsx
+++ b/src/components/header.jsx
@@ -1,4 +1,4 @@
-import { Bell, TextSearch, ServerCog, ServerCrash, ServerOff, ChevronsUpDown, Minus, Square, X } from 'lucide-react'
+import { Bell, TextSearch, ShieldEllipsis, ShieldCheck, ShieldX, ChevronsUpDown, Minus, Square, X } from 'lucide-react'
 import { useLocation } from 'react-router-dom';
 import { Button } from '@/components/ui/Button';
 import { 
@@ -20,12 +20,12 @@ export function Header({ onSearchClick, r2Status, profiles, activeProfileId, onP
 
   const getStatusIcon = () => {
     if (r2Status.loading) {
-      return <ServerCog className="h-5 w-5 text-muted-foreground" />;
+      return <ShieldEllipsis className="h-5 w-5 text-muted-foreground" />;
     }
     if (r2Status.success) {
-      return <ServerCrash className="h-5 w-5 text-green-500" />;
+      return <ShieldCheck className="h-5 w-5 text-green-500" />;
     }
-    return <ServerOff className="h-5 w-5 text-red-500" />;
+    return <ShieldX className="h-5 w-5 text-red-500" />;
   };
 
   const activeProfile = profiles.find(p => p.id === activeProfileId);
--- a/src/components/sidebar.jsx
+++ b/src/components/sidebar.jsx
@@ -15,7 +15,8 @@ import {
   ChevronRight,
   LayoutDashboard,
   Folder,
-  DownloadCloud
+  DownloadCloud,
+  Info
 } from 'lucide-react'
 import { Link, useLocation } from 'react-router-dom'
 import { useTheme } from "./theme-provider"
@@ -33,6 +34,7 @@ export function Sidebar({ isCollapsed, onToggle }) {
     { id: 'uploads', href: '/uploads', icon: Upload, label: '文件上传' },
     { id: 'downloads', href: '/downloads', icon: DownloadCloud, label: '下载管理' },
     { id: 'settings', href: '/settings', icon: Settings, label: '设置' },
+    { id: 'about', href: '/about', icon: Info, label: '关于应用' },
   ]
 
   return (
@@ -52,8 +54,12 @@ export function Sidebar({ isCollapsed, onToggle }) {
         <ul className="space-y-1 h-full flex flex-col">
           {navItems.map(({ id, href, icon: Icon, label, disabled }) => {
             const isActive = location.pathname === href;
-            const isSettings = id === 'settings';
-            const liClass = isSettings ? 'mt-auto' : '';
+            
+            let liClass = '';
+            // Push settings to the bottom, which will pull 'about' with it.
+            if (id === 'settings') {
+              liClass = 'mt-auto';
+            }
 
             const linkContent = (
               <>
--- a/src/pages/About.jsx
+++ b/src/pages/About.jsx
@@ -0,0 +1,80 @@
+import { useState, useEffect } from 'react';
+import { Card, CardContent, CardHeader, CardTitle, CardDescription, CardFooter } from "@/components/ui/Card"
+import WhiteLogo from '@/assets/WhiteLOGO.png'
+import BlackLogo from '@/assets/BlackLOGO.png'
+import { Github, GitCommit, UserCircle, Award, ArrowRight } from 'lucide-react'
+import { Button } from "@/components/ui/Button"
+
+export default function AboutPage() {
+  const [appInfo, setAppInfo] = useState({
+    name: 'R2 存储管理器',
+    version: '...',
+    author: '...',
+    description: '正在加载描述信息...',
+    license: '...',
+    githubUrl: 'https://github.com/your-repo' // 替换为您的仓库地址
+  });
+
+  useEffect(() => {
+    window.api.getAppInfo().then(info => {
+      setAppInfo(prev => ({ ...prev, ...info }));
+    });
+  }, []);
+
+  return (
+    <div className="p-4 sm:p-6 flex justify-center items-start">
+      <Card className="w-full max-w-2xl">
+        <CardHeader className="text-center">
+          <div className="flex justify-center mb-4">
+            <img src={BlackLogo} alt="Logo" className="h-20 w-20 hidden dark:block" />
+            <img src={WhiteLogo} alt="Logo" className="h-20 w-20 dark:hidden" />
+          </div>
+          <CardTitle className="text-3xl font-bold">{appInfo.name}</CardTitle>
+        </CardHeader>
+        <CardContent className="pt-4 px-8 pb-8 text-sm">
+           <p className="text-center mb-8 text-muted-foreground">
+            {appInfo.description}
+          </p>
+          <div className="space-y-5">
+            <div className="flex items-center">
+              <GitCommit className="h-5 w-5 mr-4 text-muted-foreground" />
+              <span className="w-20 text-muted-foreground">版本</span>
+              <span className="font-semibold tracking-wider">v {appInfo.version}</span>
+            </div>
+            <div className="flex items-center">
+              <UserCircle className="h-5 w-5 mr-4 text-muted-foreground" />
+              <span className="w-20 text-muted-foreground">作者</span>
+              <span className="font-semibold tracking-wider">{appInfo.author}</span>
+            </div>
+            <div className="flex items-center">
+              <Award className="h-5 w-5 mr-4 text-muted-foreground" />
+              <span className="w-20 text-muted-foreground">许可证</span>
+              <span className="font-semibold tracking-wider">{appInfo.license}</span>
+            </div>
+            <div className="flex items-center">
+              <Github className="h-5 w-5 mr-4 text-muted-foreground" />
+              <span className="w-20 text-muted-foreground">GitHub</span>
+              <a href={appInfo.githubUrl} target="_blank" rel="noopener noreferrer" className="text-blue-500 hover:underline flex items-center">
+                <span>查看源码</span>
+                <ArrowRight className="h-4 w-4 ml-1" />
+              </a>
+            </div>
+          </div>
+        </CardContent>
+        <CardFooter className="flex justify-end">
+          <Button variant="ghost" onClick={() => window.api.closeWindow()}>
+            关闭
+          </Button>
+        </CardFooter>
+      </Card>
+    </div>
+  );
+}
```
<!-- a14aef5 at https://github.com/JiQingzhe2004/R2APP/commit/a14aef53658ba41cb012d6f4602a8a9192865482 -->

---

## 🚀 添加窗口控制功能

本次提交为应用程序引入了完整的窗口控制功能，包括最小化、最大化和关闭窗口的能力。同时，更新了头部组件以集成相应的控制按钮，并新增了黑白LOGO图标以增强界面视觉效果。

### 变更摘要

`🆕 **新功能**`

我们成功为应用程序添加了窗口控制功能，使用户能够更灵活地管理窗口状态。这一改进不仅提升了用户体验，还增强了应用程序的易用性。

- **窗口控制功能**: 通过IPC通信，实现了窗口的最小化、最大化和关闭功能。用户现在可以轻松地控制窗口的显示状态。
- **头部组件更新**: 头部组件已更新，集成了窗口控制按钮，使用户可以直接在界面顶部进行窗口操作。
- **LOGO图标新增**: 为了增强界面视觉效果，新增了黑白两种LOGO图标，以适应不同的主题和视觉需求。

### 关键代码展示

```diff
--- a/electron/main/index.js
+++ b/electron/main/index.js
@@ -85,6 +85,7 @@ function createWindow() {
     height: 670,
     show: false,
     autoHideMenuBar: true,
+    frame: false,
     ...(process.platform === 'linux' ? { icon: null } : {}),
     webPreferences: {
       preload: join(__dirname, '../preload/index.mjs'),
@@ -537,4 +538,21 @@ ipcMain.handle('r2-delete-object', async (_, { key }) => {
   } catch (error) {
     return { success: false, error: `删除文件失败: ${error.message}` };
   }
+
+};
+
+// IPC handlers for window controls
+ipcMain.on('minimize-window', () => {
+  mainWindow?.minimize();
+});
+
+ipcMain.on('maximize-window', () => {
+  if (mainWindow?.isMaximized()) {
+    mainWindow.unmaximize();
+  } else {
+    mainWindow?.maximize();
+  }
+});
+
+ipcMain.on('close-window', () => {
+  mainWindow?.close();
 });
```
<!-- f3b89d6 at https://github.com/JiQingzhe2004/R2APP/commit/f3b89d60afd23c38540eb9f84b4f0b1af005161a -->

---

## 🚀 新功能：R2存储配置管理功能

本次提交为应用程序引入了全新的R2存储配置管理功能，极大地增强了用户在云存储方面的灵活性和控制力。此功能不仅支持配置文件的添加、删除和切换，还优化了设置页面的保存逻辑，并引入了单选框组件以显著改善用户体验。此外，我们还更新了相关组件，以确保它们能够无缝支持这些新功能。

### 🆕 **新功能**

-   **R2存储配置管理**: 用户现在可以轻松地添加、删除和切换R2存储配置，使得在不同存储环境之间的切换变得前所未有的简单。
-   **数据迁移**: 为了确保平滑过渡，我们实现了一个数据迁移功能，将旧版本的配置结构迁移到新的配置文件结构中，并自动创建一个默认配置文件。
-   **优化设置页面**: 通过引入单选框组件，我们改进了设置页面的用户界面，使用户能够更直观地选择和保存他们的配置。
-   **增强的IPC处理**: 我们扩展了IPC处理程序，以支持新的配置管理功能，包括保存基础设置、保存配置文件、测试R2连接等。

### 关键代码展示

```diff
const store = new Store();
+
+// --- Data Migration ---
+function runMigration() {
+  const oldSettings = store.get('settings');
+  // Check if old structure exists and new structure doesn't
+  if (oldSettings && !store.has('profiles')) {
+    console.log('Migrating old settings to new profile structure...');
+    const newProfileId = uuidv4();
+    const newBaseSettings = {
+      accountId: oldSettings.accountId,
+      accessKeyId: oldSettings.accessKeyId,
+      secretAccessKey: oldSettings.secretAccessKey,
+    };
+    const newProfile = {
+      id: newProfileId,
+      name: '默认配置',
+      bucketName: oldSettings.bucketName,
+      publicDomain: oldSettings.publicDomain || '',
+    };
+
+    store.set('settings', newBaseSettings);
+    store.set('profiles', [newProfile]);
+    store.set('activeProfileId', newProfileId);
+    console.log('Migration complete.');
+  }
+}
+
+// Run migration on startup
+runMigration();
+
let mainWindow;
+
function getActiveSettings() {
  const baseSettings = store.get('settings', {});
  const profiles = store.get('profiles', []);
  const activeProfileId = store.get('activeProfileId');
  const activeProfile = profiles.find(p => p.id === activeProfileId);
+
  if (!activeProfile) {
    return null;
  }
+
  return { ...baseSettings, ...activeProfile };
}
+
ipcMain.handle('get-settings', () => {
-    return store.get('settings')
+  return {
+    settings: store.get('settings', {}),
+    profiles: store.get('profiles', []),
+    activeProfileId: store.get('activeProfileId')
+  }
});
+
ipcMain.handle('save-base-settings', (event, settings) => {
     store.set('settings', settings)
     return { success: true }
});
+
ipcMain.handle('save-profiles', (event, { profiles, activeProfileId }) => {
  store.set('profiles', profiles);
  store.set('activeProfileId', activeProfileId);
  return { success: true };
});
+
ipcMain.handle('r2-test-connection', async (event, { settings, profile }) => {
  const testSettings = { ...settings, ...profile };
  if (!testSettings.accountId || !testSettings.accessKeyId || !testSettings.secretAccessKey || !testSettings.bucketName) {
    return { success: false, error: '缺少必要的配置信息。' }
  }
```
<!-- 1eba83a at https://github.com/JiQingzhe2004/R2APP/commit/1eba83a27b518e5e1f88c4612242c7c2adc51b75 -->

---

## 🚀 新功能：R2存储连接状态检查功能

### 变更摘要

本次提交带来了多项重要更新，旨在提升应用的稳定性和用户体验：

*   **🆕 新功能**：新增了R2存储连接状态检查功能。此功能允许应用实时验证与R2存储服务的连接状态，确保数据操作的可靠性。
*   **✨ 功能优化**：更新了相关组件以显示连接状态，用户现在可以直观地看到R2存储的连接情况。
*   **✨ 功能优化**：优化了设置页面保存功能，提升了配置操作的效率和稳定性。
*   **✨ 功能优化**：引入了新的`@radix-ui/react-tooltip`组件，改善了界面交互的友好性。

这些变更不仅增强了应用的核心功能，还提升了整体的用户体验。特别是新增的连接状态检查功能，将为用户提供了更可靠的保障。

### 关键代码展示

```diff
--- a/electron/main/index.js
+++ b/electron/main/index.js
@@ -172,6 +172,30 @@ ipcMain.handle('r2-test-connection', async (event, settings) => {
   }
 });
 
+ipcMain.handle('check-r2-status', async () => {
+  const settings = store.get('settings');
+  if (!settings || !settings.accountId || !settings.accessKeyId || !settings.secretAccessKey || !settings.bucketName) {
+    return { success: false, error: '缺少配置' };
+  }
+
+  const s3Client = new S3Client({
+    region: 'auto',
+    endpoint: `https://${settings.accountId}.r2.cloudflarestorage.com`,
+    credentials: {
+      accessKeyId: settings.accessKeyId,
+      secretAccessKey: settings.secretAccessKey,
+    },
+  });
+
+  try {
+    const command = new HeadBucketCommand({ Bucket: settings.bucketName });
+    await s3Client.send(command);
+    return { success: true, message: '连接成功' };
+  } catch (error) {
+    return { success: false, error: `连接失败: ${error.message}` };
+  }
+});
+
 ipcMain.handle('r2-get-bucket-stats', async () => {
   const settings = store.get('settings');
   if (!settings || !settings.bucketName) {
--- a/electron/preload/index.mjs
+++ b/electron/preload/index.mjs
@@ -5,8 +5,9 @@ import { electronAPI } from '@electron-toolkit/preload'
 const api = {
   getSettings: () => ipcRenderer.invoke('get-settings'),
   saveSettings: (settings) => ipcRenderer.invoke('save-settings', settings),
-  testConnection: (settings) => ipcRenderer.invoke('r2-test-connection', settings),
+  testR2Connection: (settings) => ipcRenderer.invoke('r2-test-connection', settings),
   getBucketStats: () => ipcRenderer.invoke('r2-get-bucket-stats'),
+  checkR2Status: () => ipcRenderer.invoke('check-r2-status'),
   listObjects: ({ continuationToken, prefix }) => ipcRenderer.invoke('r2-list-objects', { continuationToken, prefix }),
   deleteObject: (key) => ipcRenderer.invoke('r2-delete-object', key),
   showOpenDialog: () => ipcRenderer.invoke('show-open-dialog'),
```
<!-- 1a7daa7 at https://github.com/JiQingzhe2004/R2APP/commit/1a7daa75a3aabaae5ff706dfaf37009fdc72eaab -->

---

## 🚀 新功能：搜索对话框功能

本次提交为应用添加了核心的搜索功能，并优化了文件页面的相关逻辑。我们引入了一个全新的搜索对话框，允许用户更方便地查找文件。同时，对文件列表和搜索结果的显示方式进行了调整，以提供更直观的体验。此外，还对删除确认提示信息进行了改进，使其更加清晰和用户友好。

### 变更摘要

`🆕 **新功能**`

我们成功为应用集成了一个功能齐全的搜索对话框。现在，用户可以通过点击页面顶部的搜索按钮，轻松打开一个专门的搜索界面。这个对话框不仅支持文件名搜索，还提供了直观的界面和便捷的操作方式。

为了配合新搜索功能，我们对文件页面的搜索逻辑进行了全面的优化。现在，搜索结果会即时显示，并且用户可以在搜索对话框中直接输入和修改搜索词，而无需切换页面。这种设计大大提高了搜索的效率和用户体验。

此外，我们还调整了文件列表和搜索结果的显示方式。现在，文件列表会根据用户的搜索词动态过滤，并且搜索结果会以更清晰的方式呈现。这种改进使得用户可以更快地找到他们需要的文件。

最后，我们对删除确认提示信息进行了改进。现在，当用户尝试删除文件时，会弹出一个更加明确的确认对话框，提醒用户确认他们的操作。这种改进有助于防止用户意外删除重要文件。

### 关键代码展示

```diff
import { Bell, TextSearch } from 'lucide-react'
import { useLocation } from 'react-router-dom';
import { Button } from '@/components/ui/Button';

export function Header({ onSearchClick }) {
  const location = useLocation();
  const showSearch = location.pathname === '/files';

  return (
    <header className="h-14 flex items-center justify-between border-b bg-muted/40 px-6">
      <div>
        {showSearch && (
          <Button variant="outline" onClick={onSearchClick}>
            <TextSearch className="h-4 w-4 mr-2" />
            搜索
          </Button>
        )}
      </div>
      
      <button className="relative rounded-full h-8 w-8 flex items-center justify-center border hover:bg-accent">
        <Bell className="h-4 w-4" />
        <span className="absolute -top-1 -right-1 flex h-3 w-3">
          ...
        </span>
      </button>
    </header>
  );
}
```

```diff
export default function FilesPage({ isSearchOpen, onSearchOpenChange }) {
  const [files, setFiles] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [viewMode, setViewMode] = useState('card');
  const [searchTerm, setSearchTerm] = useState('');
  const [inputSearchTerm, setInputSearchTerm] = useState('');
  const observer = useRef();
  const navigate = useNavigate();

  const handleSearch = () => {
    setSearchTerm(inputSearchTerm);
    onSearchOpenChange(false);
    setFiles([]);
    setNextToken(null);
    fetchFiles(inputSearchTerm, false);
  };

  return (
    <AlertDialog open={!!fileToDelete} onOpenChange={(open) => !open && setFileToDelete(null)}>
      <div className="flex flex-col h-full">
        <div className="flex-shrink-0 mb-4">
          <div className="flex justify-between items-center">
            <h1 className="text-2xl font-bold">存储的文件</h1>
            <div className="flex items-center gap-4">
                <span className="text-sm text-muted-foreground">{files.length} 个文件</span>
                <ToggleGroup type="single" value={viewMode} onValueChange={(value) => value && setViewMode(value)} aria-label="View mode">
```

这些代码片段展示了新搜索对话框的集成和文件页面搜索逻辑的优化。通过这些改进，用户现在可以更轻松地找到他们需要的文件，同时享受到更流畅的操作体验。
<!-- 5ba7e66 at https://github.com/JiQingzhe2004/R2APP/commit/5ba7e660427fe2174b572bdefe77dd2ff51ee49f -->

---

## 🚀 更新依赖项，添加文件搜索功能

本次提交带来了多方面的改进，旨在提升应用的稳定性和用户体验。我们不仅更新了关键依赖项，还引入了文件搜索功能，并对文件列表加载逻辑进行了优化。此外，删除确认提示和搜索结果提示信息也得到了改进，让操作更加直观和友好。

### 🆕 **新功能**

-   **文件搜索功能**: 引入了全新的文件搜索功能，让用户能够快速定位所需文件，大幅提升工作效率。
-   **搜索结果提示信息**: 优化了搜索结果的提示信息，使其更加清晰和用户友好。

### ✨ **功能优化**

-   **文件列表加载逻辑**: 优化了文件列表的加载逻辑，提升了加载速度和响应性能。
-   **删除确认提示**: 改进了删除确认提示，增加了操作的明确性，避免误操作。

### 🐞 **Bug修复**

-   **依赖项更新**: 更新了多个关键依赖项，修复了潜在的兼容性和安全性问题。

### 关键代码展示

```diff
--- a/electron/main/index.js
+++ b/electron/main/index.js
@@ -416,21 +416,22 @@ ipcMain.on('downloads-delete-task', (_, taskId) => {
   mainWindow.webContents.send('downloads-cleared', currentTasks);
 });
 
-ipcMain.handle('r2-list-objects', async (_, { continuationToken }) => {
+ipcMain.handle('r2-list-objects', async (_, { continuationToken, prefix }) => {
   const s3Client = getS3Client();
   if (!s3Client) {
     return { success: false, error: '请先在设置中配置您的存储桶。' };
   }
-  const bucketName = store.get('settings').bucketName;
+  const settings = store.get('settings');
 
   try {
-    const command = new ListObjectsV2Command({ 
-      Bucket: bucketName,
+    const command = new ListObjectsV2Command({
+      Bucket: settings.bucketName,
       ContinuationToken: continuationToken,
+      Prefix: prefix,
       MaxKeys: 30,
     });
     const response = await s3Client.send(command);
-    return { 
+    return {
       success: true, 
       data: {
         files: response.Contents || [],
--- a/electron/preload/index.mjs
+++ b/electron/preload/index.mjs
@@ -7,10 +7,10 @@ const api = {
   saveSettings: (settings) => ipcRenderer.invoke('save-settings', settings),
   testConnection: (settings) => ipcRenderer.invoke('r2-test-connection', settings),
   getBucketStats: () => ipcRenderer.invoke('r2-get-bucket-stats'),
-  listObjects: (continuationToken) => ipcRenderer.invoke('r2-list-objects', { continuationToken }),
-  deleteObject: (key) => ipcRenderer.invoke('r2-delete-object', { key }),
+  listObjects: ({ continuationToken, prefix }) => ipcRenderer.invoke('r2-list-objects', { continuationToken, prefix }),
+  deleteObject: (key) => ipcRenderer.invoke('r2-delete-object', key),
   showOpenDialog: () => ipcRenderer.invoke('show-open-dialog'),
-  uploadFile: (filePath, key) => ipcRenderer.invoke('r2-upload-file', { filePath, key }),
+  uploadFile: (filePath) => ipcRenderer.invoke('r2-upload-file', filePath),
   onUploadProgress: (callback) => {
     const handler = (_event, value) => callback(value);
     ipcRenderer.on('upload-progress', handler);
```
<!-- aab3f96 at https://github.com/JiQingzhe2004/R2APP/commit/aab3f96c5dca6d322e3f2335f804f24269403e1a -->

---

## 🚀 更新依赖项并增强文件管理功能

本次提交带来了多项重要更新，旨在提升应用的文件管理能力和用户体验。我们不仅优化了文件上传和下载功能，还引入了全新的下载管理页面，并增强了任务状态管理和通知机制。此外，还对文件页面的显示逻辑进行了改进，包括添加文件类型图标和描述，使文件信息更加直观易懂。

### 🆕 **新功能**
- **下载管理页面**: 引入了一个全新的下载管理页面，允许用户实时监控下载任务的进度、状态和速度。
- **下载任务状态管理**: 实现了下载任务的状态管理，包括开始、下载中、完成和错误状态，并通过事件通知用户当前的下载进度。
- **文件类型图标和描述**: 为文件页面添加了类型图标和描述，使用户能够更轻松地识别和区分不同类型的文件。

### ✨ **功能优化**
- **文件上传优化**: 对文件上传功能进行了优化，增加了并发上传队列、分片上传和错误处理，提高了上传的稳定性和效率。
- **文件下载优化**: 改进了文件下载逻辑，实现了更精确的进度监控和速度计算，提升了下载体验。
- **文件页面显示逻辑**: 优化了文件页面的显示逻辑，使文件信息更加清晰和易于理解。

### 关键代码展示

```diff
--- a/electron/main/index.js
+++ b/electron/main/index.js
@@ -251,52 +252,170 @@ ipcMain.handle('r2-upload-file', async (_, { filePath, key }) => {
         Key: key,
         Body: fileStream,
       },
+      queueSize: 4, // optional concurrency
+      partSize: 1024 * 1024 * 5, // optional size of each part
+      leavePartsOnError: false, // optional manually handle dropped parts
+    });
+
+    upload.on('httpUploadProgress', (progress) => {
+      if (progress.total) {
+        const percentage = Math.round((progress.loaded / progress.total) * 100);
+        mainWindow.webContents.send('upload-progress', { key, percentage });
+      }
     });
 
     await upload.done();
     return { success: true };
   } catch (error) {
+    mainWindow.webContents.send('upload-progress', { key, percentage: 0, error: error.message });
     return { success: false, error: `文件上传失败: ${error.message}` };
   }
 });
 
-ipcMain.handle('r2-download-file', async (_, { key }) => {
+const downloadTasks = store.get('downloads', {});
+
+// Function to update and save downloads
+function updateDownloads(newTasks) {
+  store.set('downloads', newTasks);
+}
+
+ipcMain.handle('downloads-get-all', () => {
+  return store.get('downloads', {});
+});
+
+ipcMain.on('r2-download-file', async (_, { key }) => {
   const s3Client = getS3Client();
   if (!s3Client) {
-    return { success: false, error: '请先在设置中配置您的存储桶。' };
+    // We can't return an error directly, but we can send an event
+    // For now, we'll rely on the settings being correct.
+    return;
   }
   const bucketName = store.get('settings').bucketName;
 
-  const { filePath } = await dialog.showSaveDialog(mainWindow, {
-    defaultPath: key
-  });
+  const downloadsPath = app.getPath('downloads');
+  let filePath = join(downloadsPath, key);
 
-  if (!filePath) {
-    return { success: false, error: '用户取消了下载。' };
+  if (fs.existsSync(filePath)) {
+    const timestamp = new Date().getTime();
+    const pathData = parse(filePath);
+    filePath = join(pathData.dir, `${pathData.name}-${timestamp}${pathData.ext}`);
   }
 
+  const taskId = uuidv4();
+  const task = {
+    id: taskId,
+    key,
+    filePath,
+    status: 'starting',
+    progress: 0,
+    total: 0,
+    downloaded: 0,
+    createdAt: new Date().toISOString()
+  };
+  
+  const currentTasks = store.get('downloads', {});
+  currentTasks[taskId] = task;
+  updateDownloads(currentTasks);
+
+  mainWindow.webContents.send('download-start', task);
+  
   try {
     const command = new GetObjectCommand({ Bucket: bucketName, Key: key });
-    const { Body } = await s3Client.send(command);
+    const { Body, ContentLength } = await s3Client.send(command);
     
-    if (!Body) {
-      return { success: false, error: '无法获取文件内容。' };
-    }
+    if (!Body) throw new Error('无法获取文件内容。');
 
+    task.status = 'downloading';
+    task.total = ContentLength;
+    
     const writeStream = fs.createWriteStream(filePath);
+    let lastProgressTime = Date.now();
+    let lastDownloaded = 0;
+
+    Body.on('data', (chunk) => {
+      task.downloaded += chunk.length;
+      if (task.total > 0) {
+        task.progress = Math.round((task.downloaded / task.total) * 100);
+      }
+      
+      const now = Date.now();
+      const timeDiff = (now - lastProgressTime) / 1000;
+      if (timeDiff > 0.5) {
+        const bytesDiff = task.downloaded - lastDownloaded;
+        const speed = timeDiff > 0 ? bytesDiff / timeDiff : 0;
+        lastDownloaded = task.downloaded;
+        lastProgressTime = now;
+        
+        const tasks = store.get('downloads', {});
+        tasks[taskId] = { ...tasks[taskId], ...task, speed };
+        updateDownloads(tasks);
+        mainWindow.webContents.send('download-progress', { id: taskId, progress: task.progress, speed: speed, status: 'downloading' });
+      }
+    });
+
     Body.pipe(writeStream);
 
     await new Promise((resolve, reject) => {
-      writeStream.on('finish', resolve);
-      writeStream.on('error', reject);
+      writeStream.on('finish', () => {
+        task.status = 'completed';
+        task.progress = 100;
+        
+        const tasks = store.get('downloads', {});
+        tasks[taskId] = { ...tasks[taskId], ...task, speed: 0 };
+        updateDownloads(tasks);
+        mainWindow.webContents.send('download-progress', { id: taskId, progress: 100, status: 'completed' });
+        resolve();
+      });
+      const errorHandler = (err) => {
+         task.status = 'error';
+         task.error = err.message;
+
+         const tasks = store.get('downloads', {});
+         tasks[taskId] = { ...tasks[taskId], ...task };
+         updateDownloads(tasks);
+         mainWindow.webContents.send('download-progress', { id: taskId, status: 'error', error: err.message });
+         reject(err);
+      }
+      writeStream.on('error', errorHandler);
+      Body.on('error', errorHandler);
     });
 
-    return { success: true };
   } catch (error) {
-    return { success: false, error: `下载文件失败: ${error.message}` };
+    task.status = 'error';
+    task.error = error.message;
+
+    const tasks = store.get('downloads', {});
+    tasks[taskId] = task;
+    updateDownloads(tasks);
+    mainWindow.webContents.send('download-progress', { id: taskId, status: 'error', error: error.message });
   }
 });
 
+ipcMain.on('show-item-in-folder', (_, filePath) => {
+  shell.showItemInFolder(filePath);
+});
+
+ipcMain.on('downloads-clear-completed', () => {
+  const currentTasks = store.get('downloads', {});
+  const activeTasks = Object.entries(currentTasks).reduce((acc, [id, task]) => {
+    if (task.status !== 'completed') {
+      acc[id] = task;
+    }
+    return acc;
+  }, {});
+  updateDownloads(activeTasks);
+  mainWindow.webContents.send('downloads-cleared', activeTasks);
+});
+
+ipcMain.on('downloads-delete-task', (_, taskId) => {
+  const currentTasks = store.get('downloads', {});
+  // Here you could also add logic to delete the actual file from disk if desired
+  // fs.unlinkSync(currentTasks[taskId].filePath);
+  delete currentTasks[taskId];
+  updateDownloads(currentTasks);
+  mainWindow.webContents.send('downloads-cleared', currentTasks);
+});
+
 ipcMain.handle('r2-list-objects', async (_, { continuationToken }) => {
   const s3Client = getS3Client();
   if (!s3Client) {
--- a/electron/preload/index.mjs
+++ b/electron/preload/index.mjs
@@ -18,7 +18,30 @@ const api = {
       ipcRenderer.removeListener('upload-progress', handler);
     };
   },
-  downloadFile: (key) => ipcRenderer.invoke('r2-download-file', { key })
+  downloadFile: (key) => ipcRenderer.send('r2-download-file', { key }),
+  getAllDownloads: () => ipcRenderer.invoke('downloads-get-all'),
+  onDownloadUpdate: (callback) => {
+    const startHandler = (_event, task) => callback({ type: 'start', task });
+    const progressHandler = (_event, data) => callback({ type: 'progress', data });
+
+    ipcRenderer.on('download-start', startHandler);
+    ipcRenderer.on('download-progress', progressHandler);
+
+    return () => {
+      ipcRenderer.removeListener('download-start', startHandler);
+      ipcRenderer.removeListener('download-progress', progressHandler);
+    };
+  },
+  showItemInFolder: (filePath) => ipcRenderer.send('show-item-in-folder', filePath),
+  clearCompletedDownloads: () => ipcRenderer.send('downloads-clear
```
<!-- ca00387 at https://github.com/JiQingzhe2004/R2APP/commit/ca00387ae115afc12e8c76c3554ff54675a9b43b -->

---

## 🚀 更新依赖项与功能增强

本次提交带来了多方面的改进，旨在提升用户体验和应用的稳定性。我们不仅引入了新的依赖项，还增强了快捷键、侧边栏折叠功能以及文件页面的加载显示逻辑，并在设置页面中加入了toast通知以提供更直观的反馈。

### 🆕 **新功能**
- **添加 `sonner` 库**: 引入 `sonner` 库用于在设置页面中提供toast通知，以反馈连接和保存状态。
- **注册 F5 快捷键**: 在主进程中注册了 F5 快捷键，用于刷新窗口，提升操作便捷性。
- **改进侧边栏折叠功能**: 侧边栏现在支持折叠，用户可以根据需要调整界面布局，提升空间利用率。

### ✨ **功能优化**
- **优化文件页面的加载和显示逻辑**: 对文件页面的加载和显示逻辑进行了优化，提升了页面的响应速度和用户体验。
- **改进设置页面的通知机制**: 使用 `sonner` 库在设置页面中添加toast通知，以更直观地反馈连接和保存状态。

### 关键代码展示

```diff
--- a/electron/main/index.js
+++ b/electron/main/index.js
@@ -1,4 +1,4 @@
-import { app, shell, BrowserWindow, ipcMain, dialog } from 'electron'
+import { app, shell, BrowserWindow, ipcMain, dialog, globalShortcut } from 'electron'
 import { join } from 'path'
 import { electronApp, is } from '@electron-toolkit/utils'
 import Store from 'electron-store'
@@ -104,13 +104,26 @@ app.whenReady().then(() => {
   console.log('App is ready');
   electronApp.setAppUserModelId('com.r2.explorer')
 
+  // Register F5 for refresh
+  globalShortcut.register('F5', () => {
+    const focusedWindow = BrowserWindow.getFocusedWindow();
+    if (focusedWindow) {
+      focusedWindow.webContents.reload();
+    }
+  });
+
   createWindow()
 
   app.on('activate', function () {
     if (BrowserWindow.getAllWindows().length === 0) createWindow()
   })
 })
 
+app.on('will-quit', () => {
+  // Unregister all shortcuts.
+  globalShortcut.unregisterAll();
+});
+
 app.on('window-all-closed', () => {
   if (process.platform !== 'darwin') {
     app.quit()
@@ -295,14 +308,13 @@ ipcMain.handle('r2-list-objects', async (_, { continuationToken }) => {
     const command = new ListObjectsV2Command({ 
       Bucket: bucketName,
       ContinuationToken: continuationToken,
-      // Delimiter: '/', // Optional: for folder-like navigation
+      MaxKeys: 30,
     });
     const response = await s3Client.send(command);
     return { 
       success: true, 
       data: {
         files: response.Contents || [],
-        // commonPrefixes: response.CommonPrefixes || [],
         nextContinuationToken: response.NextContinuationToken
       }
     };
--- a/src/App.jsx
+++ b/src/App.jsx
@@ -1,4 +1,6 @@
+import { useState } from 'react';
 import { ThemeProvider } from "@/components/theme-provider"
+import { Toaster } from 'sonner';
 import { Layout, LayoutBody } from '@/components/ui/layout'
 import { Sidebar } from '@/components/sidebar'
 import { Header } from '@/components/header'
@@ -9,11 +11,18 @@ import FilesPage from './pages/Files';
 import UploadsPage from './pages/Uploads';
 
 function App() {
+  const [isSidebarCollapsed, setIsSidebarCollapsed] = useState(false);
+
+  const toggleSidebar = () => {
+    setIsSidebarCollapsed(prev => !prev);
+  }
+
   return (
     <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
+      <Toaster richColors position="top-center" />
       <Router>
         <Layout>
-          <Sidebar />
+          <Sidebar isCollapsed={isSidebarCollapsed} onToggle={toggleSidebar} />
           <LayoutBody>
             <Header />
             <main className="flex-1 p-6 overflow-auto">
--- a/src/components/sidebar.jsx
+++ b/src/components/sidebar.jsx
@@ -5,40 +5,52 @@ import {
   Download,
   Settings,
   Sun,
-  Moon
+  Moon,
+  PanelLeftClose,
+  PanelRightClose,
+  PackageOpen,
+  FolderUp,
+  FolderDown
 } from 'lucide-react'
 import { Link, useLocation } from 'react-router-dom'
 import { useTheme } from "./theme-provider"
+import { cn } from "@/lib/utils"
 
-export function Sidebar() {
+export function Sidebar({ isCollapsed, onToggle }) {
   const { theme, setTheme } = useTheme()
   const location = useLocation();
 
   const navItems = [
     { id: 'dashboard', href: '/dashboard', icon: Home, label: '仪表盘' },
-    { id: 'files', href: '/files', icon: File, label: '文件管理' },
-    { id: 'uploads', href: '/uploads', icon: Upload, label: '上传文件' },
-    { id: 'downloads', href: '#', icon: Download, label: '下载管理', disabled: true },
+    { id: 'files', href: '/files', icon: PackageOpen, label: '文件管理' },
+    { id: 'uploads', href: '/uploads', icon: FolderUp, label: '上传文件' },
+    { id: 'downloads', href: '#', icon: FolderDown, label: '下载管理', disabled: true },
     { id: 'settings', href: '/settings', icon: Settings, label: '设置' },
   ]
 
   return (
-    <aside className="w-64 flex-shrink-0 border-r bg-muted/40 flex flex-col">
-      <div className="h-14 flex items-center border-b px-6">
-        <h1 className="text-lg font-bold">R2存储管理器</h1>
+    <aside className={cn(
+      "flex-shrink-0 border-r bg-muted/40 flex flex-col transition-all duration-300 ease-in-out",
+      isCollapsed ? "w-20" : "w-64"
+    )}>
+      <div className={cn(
+        "h-14 flex items-center border-b px-6",
+        isCollapsed && "px-0 justify-center"
+      )}>
+        <h1 className={cn("text-lg font-bold", isCollapsed && "hidden")}>R2存储管理器</h1>
+        <h1 className={cn("text-lg font-bold", !isCollapsed && "hidden")}>R2</h1>
       </div>
       <nav className="flex-1 py-4 px-4">
-        <ul className="space-y-1">
+        <ul className="space-y-1 h-full flex flex-col">
           {navItems.map(({ id, href, icon: Icon, label, disabled }) => {
             const isActive = location.pathname === href;
-            // Find settings and add a margin-top to it to push it to the bottom.
             const isSettings = id === 'settings';
             const liClass = isSettings ? 'mt-auto' : '';
 
             const linkContent = (
               <>
-                <Icon className="h-4 w-4" />
-                <span>
+                <Icon className={cn("h-5 w-5", isCollapsed && "h-6 w-6")} />
+                <span className={cn(isCollapsed && "hidden")}>
                   {label}
                   {disabled && ' (待开发)'}
                 </span>
```
<!-- 367d89f at https://github.com/JiQingzhe2004/R2APP/commit/367d89f63d2af19eba08e01d7fb1b23ed5490c6f -->

---

## 🐞 **Bug修复**

本次提交主要修复了 R2 存储资源管理器应用程序在构建后无法正常运行的问题。该应用程序原本只能在开发环境下运行，构建后的版本遇到了兼容性问题。我们通过以下修改解决了这个问题：

1.  **添加 `.gitignore` 配置**：确保了 `node_modules`、`.vscode`、`out`、`dist` 和 `release` 目录被正确忽略，避免构建时的潜在冲突。
2.  **完善 `README.md` 文档**：提供了更详细的安装、运行和构建说明，特别是明确了如何在生产环境下构建和运行应用程序。
3.  **配置 `electron.vite.config.js`**：为 Electron 应用程序提供了更完善的配置，包括入口文件、插件和别名设置。
4.  **增强 `electron/main/index.js` 逻辑**：
    - 添加了增强的调试日志，打印应用程序路径和目录结构，帮助排查问题。
    - 配置了 `electron-serve` 进行详细日志记录，跟踪文件请求。
    - 确保了在开发模式下和生产模式下都能正确加载应用程序。
    - 修复了 `preload` 和 `renderer` 的配置，确保应用程序正常运行。
    - 完善了 IPC 处理器，特别是 `r2-test-connection` 和 `r2-get-bucket-stats`，确保配置信息有效且能正确连接到 R2 存储桶。

这些修改确保了应用程序在开发环境和生产环境下都能稳定运行，提升了用户体验和应用程序的可靠性。

```diff
--- a/electron/main/index.js
+++ b/electron/main/index.js
@@ -0,0 +1,328 @@
+import { app, shell, BrowserWindow, ipcMain, dialog } from 'electron'
+import { join } from 'path'
+import { electronApp, is } from '@electron-toolkit/utils'
+import Store from 'electron-store'
+import { S3Client, ListObjectsV2Command, DeleteObjectCommand, GetObjectCommand } from '@aws-sdk/client-s3'
+import { Upload } "@aws-sdk/lib-storage";
+import fs from 'fs';
+import serve from 'electron-serve';
+
+// Enhanced debugging - Print app paths
+console.log('App paths:');
+console.log('- App path:', app.getAppPath());
+console.log('- App directory structure:');
+try {
+  // Check if dist directory exists
+  const distPath = join(app.getAppPath(), 'dist');
+  console.log('- Dist path exists:', fs.existsSync(distPath));
+  if (fs.existsSync(distPath)) {
+    console.log('- Dist directory contents:', fs.readdirSync(distPath));
+    
+    // Check if index.html exists
+    const indexPath = join(distPath, 'index.html');
+    console.log('- index.html exists:', fs.existsSync(indexPath));
+  }
+} catch (err) {
+  console.error('Error checking directory structure:', err);
+}
+
+// Configure electron-serve with detailed logging
+const loadURL = serve({
+  directory: 'dist',
+  // Add a custom handler to log file requests
+  handler: (request, response) => {
+    const url = request.url.replace('app://', '');
+    console.log(`[electron-serve] Request for: ${url}`);
+    return null; // Let electron-serve handle the request normally
+  }
+});
+
+// This is the correct way to disable sandbox for the entire app.
+app.commandLine.appendSwitch('no-sandbox');
+
+try {
+  require('electron-reloader')(module, {});
+} catch (_) {}
+
+const store = new Store()
+
+let mainWindow;
+
+function createWindow() {
+  console.log('Creating main window...');
+  mainWindow = new BrowserWindow({
+    width: 900,
+    height: 670,
+    show: false,
+    autoHideMenuBar: true,
+    ...(process.platform === 'linux' ? { icon: null } : {}),
+    webPreferences: {
+      preload: join(__dirname, '../preload/index.mjs'),
+      sandbox: false,
+      contextIsolation: true,
+      // Enable dev tools in production for debugging
+      devTools: true
+    }
+  })
+
+  mainWindow.on('ready-to-show', () => {
+    console.log('Window ready to show');
+    mainWindow.show()
+    // Open DevTools in production for debugging
+    if (!is.dev) {
+      mainWindow.webContents.openDevTools()
+    }
+  })
+
+  // Add error listener for failed page loads
+  mainWindow.webContents.on('did-fail-load', (event, errorCode, errorDescription, validatedURL) => {
+    console.error(`Failed to load URL: ${validatedURL}`);
+    console.error(`Error code: ${errorCode}, Description: ${errorDescription}`);
+  });
+
+  mainWindow.webContents.setWindowOpenHandler((details) => {
+    shell.openExternal(details.url)
+    return { action: 'deny' }
+  })
+  
+  mainWindow.on('closed', () => {
+    console.log('Window closed');
+    mainWindow = null;
+  });
+
+  if (is.dev && process.env['ELECTRON_RENDERER_URL']) {
+    console.log(`Loading dev URL: ${process.env['ELECTRON_RENDERER_URL']}`);
+    mainWindow.loadURL(process.env['ELECTRON_RENDERER_URL'])
+    mainWindow.webContents.openDevTools()
+  } else {
+    console.log('Loading production app via electron-serve');
+    loadURL(mainWindow)
+  }
+}
+
+app.whenReady().then(() => {
+  console.log('App is ready');
+  electronApp.setAppUserModelId('com.r2.explorer')
+
+  createWindow()
+
+  app.on('activate', function () {
+    if (BrowserWindow.getAllWindows().length === 0) createWindow()
+  })
+})
+
+app.on('window-all-closed', () => {
+  if (process.platform !== 'darwin') {
+    app.quit()
+  }
+})
+
+// IPC handlers
+ipcMain.handle('get-settings', () => {
+    return store.get('settings')
+})
+
+ipcMain.handle('save-settings', (event, settings) => {
+    store.set('settings', settings)
+    return { success: true }
+})
+
+ipcMain.handle('r2-test-connection', async (event, settings) => {
+  if (!settings || !settings.accountId || !settings.accessKeyId || !settings.secretAccessKey || !settings.bucketName) {
+    return { success: false, error: '缺少必要的配置信息。' }
+  }
+
+  const testS3Client = new S3Client({
+    region: 'auto',
+    endpoint: `https://${settings.accountId}.r2.cloudflarestorage.com`,
+    credentials: {
+      accessKeyId: settings.accessKeyId,
+      secretAccessKey: settings.secretAccessKey,
+    },
+  });
+
+  try {
+    const command = new ListObjectsV2Command({ Bucket: settings.bucketName, MaxKeys: 0 });
+    await testS3Client.send(command);
+    return { success: true, message: '连接成功！配置信息有效。' };
+  } catch (error) {
+    let errorMessage = '连接失败。';
+    if (error.name === 'NoSuchBucket') {
+      errorMessage = '连接失败：找不到指定的存储桶。';
+    } else if (error.name === 'InvalidAccessKeyId' || error.name === 'SignatureDoesNotMatch') {
+      errorMessage = '连接失败：访问密钥 ID 或秘密访问密钥无效。';
+    } else {
+      errorMessage = `连接失败：${error.message}`;
+    }
+    return { success: false, error: errorMessage };
+  }
+});
+
+ipcMain.handle('r2-get-bucket-stats', async () => {
+  const settings = store.get('settings');
+  if (!settings || !settings.bucketName) {
+    return { success: false, error: '缺少必要的配置信息。' };
+  }
+  // ... (rest of the code)
+});
```
<!-- 860c023 at https://github.com/JiQingzhe2004/R2APP/commit/860c023f2ccd8321c602da0d7cf5a28014ffb378 -->