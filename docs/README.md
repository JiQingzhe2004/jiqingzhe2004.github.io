# CS-Explorer应用更新说明

## 🚀 新增更新日志页面

### 变更摘要

本次提交带来了应用中一个重要的新功能——**更新日志页面**的集成。我们不仅添加了一个新的页面来展示应用的最新更新信息，还对侧边栏进行了优化，新增了一个明显的“更新日志”链接，方便用户快速访问。

-   **`🆕 新功能`**: 新增了完整的更新日志页面，使用户能够轻松查阅应用的最新动态和变更。
-   **`✨ 功能优化`**: 侧边栏布局经过优化，现在包含了指向更新日志的链接，提升了用户体验和导航的便捷性。

### 关键代码展示

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

本次提交为项目添加了必要的许可证文件，确保项目的合法使用和分发。这是一个重要的基础性工作，有助于明确项目的使用条款和版权归属。

`🆕 **新功能**`

许可证文件是开源项目的重要组成部分，它规定了用户可以如何使用、修改和分发项目代码。通过明确许可条款，我们为项目的合作者和使用者提供了清晰的法律框架，促进了项目的健康发展和社区贡献。

由于添加许可证文件属于基础配置和合规性要求，不涉及核心业务逻辑的变更，因此没有相关的关键代码展示。
<!-- 070eaa3 at https://github.com/JiQingzhe2004/R2APP/commit/070eaa3de84fa03b7245cb6f7707a1ff8d26d24c -->

---

## ✨ 功能优化

本次提交主要聚焦于提升应用的版本管理和用户体验。我们更新了 `.gitignore` 文件以排除日志和构建输出文件，确保代码仓库的整洁。同时，在 `package.json` 中的构建脚本中注入了版本信息，并新增了 `inject-version.cjs` 脚本用于生成版本文件。这些改动使得应用版本信息能够被准确追踪和展示，最终在用户界面中更新了应用版本信息的显示，优化了用户界面。

### 分类和图标
- `✨ **功能优化**`

### 关键代码展示
<details>
<summary>💡 查看关键代码变更</summary>

\`\`\`diff
// 在 package.json 中修改构建脚本以注入版本信息
"dev": "node ./scripts/inject-version.cjs && electron-vite dev",
"build": "node ./scripts/inject-version.cjs && electron-vite build",
\`\`\`

\`\`\`diff
// 新增 inject-version.cjs 脚本以生成版本文件
const fs = require('fs');
const path = require('path');

const version = process.env.VERSION || `dev-${new Date().toISOString()}`;
const versionData = { version: version };
const outputPath = path.join(__dirname, '../src/version.json');
fs.writeFileSync(outputPath, JSON.stringify(versionData, null, 2));
\`\`\`

\`\`\`diff
// 在 About 页面中显示应用版本信息
import versionData from '@/version.json';

export default function AboutPage() {
  const [appInfo, setAppInfo] = useState({
    name: 'R2 存储管理器',
    version: versionData.version,
  });
  // ...
}
\`\`\`
</details>
<!-- 100329b at https://github.com/JiQingzhe2004/R2APP/commit/100329be787efa753a624b7c6ecb241f6d5c1e8b -->

---

## 🚀 v3.0.0

本次更新带来了令人兴奋的新功能和用户体验优化！我们专注于提升用户在文件预览组件中的操作便捷性，并引入了直观的视觉元素来增强交互体验。以下是本次版本的核心变更：

*   **🆕 **新功能**: 在文件预览组件中新增了“复制代码到剪贴板”功能，让用户可以轻松地复制文件内容，极大地提升了工作效率和灵活性。
*   **✨ **功能优化**: 引入了Copy图标并优化了界面交互性，使得用户在操作时能够更直观地感知到可用的功能点，提升了整体的用户体验。

我们相信这些改进将为用户带来更加流畅和高效的使用体验。让我们深入了解一下本次版本的关键代码变更吧！

<details>
<summary>💡 查看关键代码变更</summary>

\`\`\`diff
+import { Copy } from 'lucide-react';
+import { toast } from 'sonner';
+
+const handleCopy = () => {
+  if (content) {
+    navigator.clipboard.writeText(content);
+    toast.success('代码已复制到剪贴板');
+  }
+};
+
+if (isCode(fileName)) {
+  return (
+    <div className="relative">
+      <Button
+        variant="ghost"
+        size="icon"
+        className="absolute top-2 right-2 h-7 w-7"
+        onClick={handleCopy}
+      >
+        <Copy className="h-4 w-4" />
+      </Button>
+      <SyntaxHighlighter language={fileName.split('.').pop()} style={atomDark} showLineNumbers>
+        {content}
+      </SyntaxHighlighter>
+    </div>
+  );
+}
\`\`\`

</details>
<!-- 1031df0 at https://github.com/JiQingzhe2004/R2APP/commit/1031df01689f39efdfa178fa0b5a117fdc303d35 -->

---

## 🚀 新增文件预览功能

本次提交为应用程序引入了强大的文件预览功能，极大地提升了用户体验。现在用户可以直接在文件页面中预览代码和图片文件，无需跳转到外部工具。此外，我们还集成了 `react-syntax-highlighter` 依赖项，以支持代码高亮显示，使得代码预览更加清晰易读。

### 变更分类:
- `🆕 **新功能**`

#### 关键代码展示
<details>
<summary>💡 查看关键代码变更</summary>

\`\`\`diff
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
\`\`\`

</details>
<!-- 71f832c at https://github.com/JiQingzhe2004/R2APP/commit/71f832c295634a85e78416bb7113b82450071990 -->

---

## 📁 新增文件夹管理功能

本次提交带来了全面的文件夹管理功能，极大地提升了用户对文件系统的掌控力。我们不仅实现了文件夹的创建和删除，还对文件列表显示进行了优化，现在能够清晰地区分文件夹和文件。同时，文件上传逻辑也得到了更新，用户可以选择特定的文件夹进行上传，而文件删除逻辑也支持文件夹的批量删除操作。为了增强UI效果，我们还更新了依赖项，引入了`@radix-ui/react-separator`组件。

### 🆕 **新功能**
- **文件夹管理**: 支持创建和删除文件夹，让用户能够更灵活地组织文件。
- **文件列表显示优化**: 区分显示文件夹和文件，提升用户体验。
- **文件上传优化**: 支持选择文件夹进行上传，简化操作流程。
- **文件删除优化**: 支持文件夹的删除操作，实现批量删除。
- **依赖项更新**: 添加`@radix-ui/react-separator`组件，增强UI效果。

### 🐞 **Bug修复**
- 修复了文件删除逻辑中的潜在问题，确保文件夹删除操作的稳定性。

<details>
<summary>💡 查看关键代码变更</summary>

\`\`\`diff
+ipcMain.handle('list-objects', async (_, { continuationToken, prefix, delimiter }) => {
   const storage = await getStorageClient();
   if (!storage) {
-    return { success: false, error: '请先在设置中配置您的存储桶。' };
+    return { success: false, error: '未找到活动的存储配置' };
   }
 
   try {
     let files = [];
-    let nextContinuationToken;
+    let folders = [];
+    let nextContinuationToken = null;
 
     if (storage.type === 'r2') {
-      const command = new ListObjectsV2Command({ Bucket: storage.bucket, ContinuationToken: continuationToken, Prefix: prefix, MaxKeys: 30 });
+      const command = new ListObjectsV2Command({
+        Bucket: storage.bucket,
+        ContinuationToken: continuationToken,
+        Prefix: prefix,
+        Delimiter: delimiter,
+        MaxKeys: 50,
+      });
       const response = await storage.client.send(command);
       files = (response.Contents || []).map(f => ({
-          key: f.Key,
-          lastModified: f.LastModified,
-          size: f.Size,
-          etag: f.ETag
+        key: f.Key,
+        lastModified: f.LastModified,
+        size: f.Size,
+        etag: f.ETag
+      }));
+      folders = (response.CommonPrefixes || []).map(p => ({
+        key: p.Prefix,
+        type: 'folder'
       }));
       nextContinuationToken = response.NextContinuationToken;
     } else if (storage.type === 'oss') {
-      const response = await storage.client.list({ marker: continuationToken, prefix: prefix, 'max-keys': 30 });
+      const response = await storage.client.list({
+        marker: continuationToken,
+        prefix: prefix,
+        delimiter: delimiter,
+        'max-keys': 50
+      });
       files = (response.objects || []).map(f => ({
-          key: f.name,
-          lastModified: f.lastModified,
-          size: f.size,
-          etag: f.etag
+        key: f.name,
+        lastModified: f.lastModified,
+        size: f.size,
+        etag: f.etag
+      }));
+      folders = (response.prefixes || []).map(p => ({
+        key: p,
+        type: 'folder'
       }));
       nextContinuationToken = response.nextMarker;
     }
     
-    return { success: true, data: { files, nextContinuationToken } };
+    // Combine folders and files, with folders first
+    const combined = [
+      ...folders.map(f => ({ ...f, isFolder: true })),
+      ...files.map(f => ({ ...f, isFolder: false }))
+    ].filter(item => item.key !== prefix); // Don't show the current folder itself
+
+    return { success: true, data: { files: combined, nextContinuationToken } };
   } catch (error) {
     return { success: false, error: `获取文件列表失败: ${error.message}` };
   }
\`\`\`

\`\`\`diff
+ipcMain.handle('delete-folder', async (event, prefix) => {
   const storage = await getStorageClient();
   if (!storage) {
     return { success: false, error: '未找到有效的存储配置' };
   }
   const { client, type, bucket } = storage;
   
   try {
     let allKeys = [];
     if (type === 'r2') {
       let continuationToken;
       do {
         const response = await client.send(new ListObjectsV2Command({
           Bucket: bucket,
           Prefix: prefix,
           ContinuationToken: continuationToken,
         }));
         if (response.Contents) {
           allKeys.push(...response.Contents.map(item => item.Key));
         }
         continuationToken = response.NextContinuationToken;
       } while (continuationToken);
       
       if (allKeys.length > 0) {
         // AWS S3 DeleteObjects can handle 1000 keys at a time
         for (let i = 0; i < allKeys.length; i += 1000) {
           const chunk = allKeys.slice(i, i + 1000);
           await client.send(new DeleteObjectsCommand({
             Bucket: bucket,
             Delete: { Objects: chunk.map(k => ({ Key: k })) },
           }));
         }
       }
     } else if (type === 'oss') {
       let continuationToken;
       do {
         const response = await client.list({
           prefix: prefix,
           marker: continuationToken,
           'max-keys': 1000,
         });
         if (response.objects) {
           allKeys.push(...response.objects.map(item => item.name));
         }
         continuationToken = response.nextMarker;
       } while (continuationToken);
       
       if (allKeys.length > 0) {
         // OSS deleteMulti can handle 1000 keys at a time
         await client.deleteMulti(allKeys, { quiet: true });
       }
     }
     
     addRecentActivity('delete', `文件夹 "${prefix}" 已删除`, 'success');
     return { success: true, deletedCount: allKeys.length };
   } catch (error) {
     console.error(`Failed to delete folder ${prefix}:`, error);
     addRecentActivity('delete', `删除文件夹 "${prefix}" 失败`, 'error');
     return { success: false, error: error.message };
   }
 });
\`\`\`

</details>
<!-- ccb3eac at https://github.com/JiQingzhe2004/R2APP/commit/ccb3eac0c6a69e41794be4ea9f59056bc31051f5 -->

---

## 🚀 v2.0.1

本次更新为应用带来了**质的飞跃**！我们不仅将应用名称升级为更专业的 **CS-Explorer**，还引入了多项令人兴奋的新功能与优化，旨在提供更流畅、更高效的用户体验。

### 变更摘要

本次更新涵盖以下核心内容：

- **🆕 **新功能**:  
  - **最近活动记录功能**：现在，您可以看到所有上传、下载和删除操作的实时记录，让数据管理更清晰！
  - **仪表盘优化**：仪表盘现在显示存储使用情况和最近活动，帮助您快速掌握数据状态。

- **✨ **功能优化**:  
  - **设置页面升级**：新增存储配额配置选项，让您更灵活地管理资源。
  - **窗口状态管理**：增强窗口控制功能，支持最大化/最小化状态监听，提升多任务处理效率。

- **🐞 **Bug修复**:  
  - 修复了存储桶统计信息获取失败的问题，确保数据准确性。
  - 优化了文件删除操作的错误处理，提供更清晰的反馈。

这些改进不仅让 CS-Explorer 更加强大，也使其更加易用和可靠。我们相信，这些更新将为您的数据管理带来全新的体验！

### 关键代码展示

<details>
<summary>💡 查看关键代码变更</summary>

\`\`\`diff
// 添加最近活动记录功能
const MAX_ACTIV =ITIES 20;

function addRecentActivity(type, message, status) {
  const activities = store.get('recent-activities', []);
  const newActivity = {
    id: uuidv4(),
    type,
    message,
    status,
    timestamp: new Date().toISOString(),
  };
  const updatedActivities = [newActivity, ...activities].slice(0, MAX_ACTIVITIES);
  store.set('recent-activities', updatedActivities);
}

// 优化存储桶统计信息获取
try {
  let totalCount = 0;
  let totalSize = 0;
  let continuationToken = undefined;

  if (storage.type === 'r2') {
    do {
      const command = new ListObjectsV2Command({
        Bucket: storage.bucket,
        ContinuationToken: continuationToken,
      });
      const response = await storage.client.send(command);
      totalCount += response.KeyCount || 0;
      totalSize += response.Contents?.reduce((acc, obj) => acc + obj.Size, 0) || 0;
      continuationToken = response.NextContinuationToken;
    } while (continuationToken);
  } else if (storage.type === 'oss') {
    do {
      const response = await storage.client.list({ marker: continuationToken, 'max-keys': 1000 });
      totalCount += response.objects?.length || 0;
      totalSize += response.objects?.reduce((acc, obj) => acc + obj.size, 0) || 0;
      continuationToken = response.nextMarker;
    } while (response.isTruncated);
  }

  const quota = parseInt(activeProfile?.storageQuotaGB, 10);
  return { 
    success: true, 
    data: { 
      totalCount, 
      totalSize, 
      bucketName: storage.bucket,
      storageQuotaGB: !isNaN(quota) && quota > 0 ? quota : 10
    } 
  };
} catch (error) {
  console.error('Failed to get bucket stats:', error);
  return { success: false, error: error.message };
}
\`\`\`

</details>

这些代码片段展示了新增的最近活动记录功能和优化的存储桶统计信息获取逻辑，是本次更新的核心亮点。通过这些改进，CS-Explorer 现在能更好地帮助您管理数据，并提供更直观的反馈。
<!-- 48117cc at https://github.com/JiQingzhe2004/R2APP/commit/48117cc0f853359c74720768918932d9ac241033 -->

---

## 🚀 v2.0.1

本次更新带来了多项改进，旨在提升用户体验和应用的稳定性。以下是本次版本的主要变更：

- **🆕 新功能**: 头部组件的配置选择功能得到了显著增强，新增了单选框，使得用户在切换配置时更加直观和便捷。
- **✨ 功能优化**: 文件页面的文件名显示方式进行了优化，增加了截断效果，确保在文件名过长时不会影响页面布局的整洁性。
- **✨ 功能优化**: 关于页面的GitHub链接已经更新，指向了最新的仓库地址，方便用户获取最新的项目信息。

### 关键代码展示

<details>
<summary>💡 查看关键代码变更</summary>

\`\`\`diff
- {profiles.map(profile => (
-   <DropdownMenuItem key={profile.id} onSelect={() => onProfileSwitch(profile.id)} disabled={profile.id === activeProfileId}>
-     {profile.name}
-   </DropdownMenuItem>
- ))}
+ <DropdownMenuLabel>选择配置</DropdownMenuLabel>
+ <DropdownMenuSeparator />
+ <DropdownMenuRadioGroup value={activeProfileId} onValueChange={onProfileSwitch}>
+   {profiles.map(profile => (
+     <DropdownMenuRadioItem key={profile.id} value={profile.id}>
+       {profile.name}
+     </DropdownMenuRadioItem>
+   ))}
+ </DropdownMenuRadioGroup>
\`\`\`

\`\`\`diff
- <TableCell className="font-medium">{key}</TableCell>
+ <TableCell className="font-medium max-w-xs truncate" title={key}>
+   {key}
+ </TableCell>
\`\`\`

</details>
<!-- d3ac191 at https://github.com/JiQingzhe2004/R2APP/commit/d3ac1915e8beaf963eb4ce3df2e89345e945eafd -->

---

## ✨ 更新应用名称和版本

### 变更摘要

本次提交对应用进行了全面的更新，旨在提升用户体验并反映新功能的引入。以下是变更的详细内容：

- `🆕 **新功能**`: 应用名称从 `r2-explorer` 更新为 `CS-Explorer`，以更好地反映其管理在线云存储的功能。版本号也从 `1.0.0` 升级到 `2.0.0`，标志着应用的重大更新。
- `✨ **功能优化**`: 应用描述进行了修改，从“一个用于管理Cloudflare R2存储的现代化桌面应用”更新为“一个用于管理在线云存储的现代化桌面应用”，更准确地描述了应用的功能范围。
- `✨ **功能优化**`: 应用图标和LOGO也进行了替换，以提升视觉效果，使应用更具吸引力。

这些变更不仅提升了应用的品牌形象，还为用户提供了更清晰的功能预期。

### 关键代码展示

<details>
<summary>💡 查看关键代码变更</summary>

\`\`\`diff
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

</details>
<!-- 8027d10 at https://github.com/JiQingzhe2004/R2APP/commit/8027d10dce10e71d206c7c772c34ffeb98ad8d3c -->

---

## 🚀 添加阿里云OSS支持

本次提交主要引入了对阿里云OSS（Object Storage Service）的支持，并进行了相关的配置和逻辑重构，以提升应用的多存储类型兼容性和用户体验。

### 变更摘要

`🆕 **新功能**` - 本次变更的核心是新增了对阿里云OSS的支持，使得用户可以方便地配置和使用阿里云OSS服务进行文件存储。同时，还进行了以下优化：

- **配置文件更新**: 在 `electron.vite.config.js` 中添加了 `ali-oss` 到 `external` 依赖列表，确保应用能够正确引入OSS客户端库。
- **文件处理逻辑重构**: 修改了 `electron/main/index.js` 中的数据迁移逻辑，使其能够处理OSS存储类型，并正确迁移旧配置到新的配置结构中。
- **设置页面优化**: 更新了设置页面，以支持OSS配置的添加和管理，提升了用户在多存储类型环境下的操作便利性。

通过这些变更，用户现在可以在应用中轻松配置和使用阿里云OSS，享受更加灵活和高效的文件存储体验。

### 关键代码展示

<details>
<summary>💡 查看关键代码变更</summary>

\`\`\`diff
// electron.vite.config.js
-        external: ['@electron-toolkit/utils', 'electron-store']
+        external: ['@electron-toolkit/utils', 'electron-store', 'ali-oss']

// electron/main/index.js
-  // Data Migration
-  function runMigration() {
-    const oldSettings = store.get('settings');
-    // Check if old structure exists and new structure doesn't
-    if (oldSettings && !store.has('profiles')) {
+  // Data Migration
+  function runMigration() {
+    const oldSettings = store.get('settings');
+    const oldProfiles = store.get('profiles');
+
+    // Check if old structure with base settings exists and new unified profiles don't
+    if (oldSettings && oldSettings.accountId && (!oldProfiles || oldProfiles.length === 0 || !oldProfiles[0].type)) {
       console.log('Migrating old settings to new profile structure...');
-      const newProfileId = uuidv4();
-      const newBaseSettings = {
+      const migratedProfiles = (oldProfiles || []).map(p => ({
+        id: p.id || uuidv4(),
+        name: p.name || '默认R2配置',
+        bucketName: p.bucketName,
+        publicDomain: p.publicDomain || '',
+        // Add R2 specific fields from old base settings
+        type: 'r2',
         accountId: oldSettings.accountId,
         accessKeyId: oldSettings.accessKeyId,
         secretAccessKey: oldSettings.secretAccessKey,
-      };
-      const newProfile = {
-        id: newProfileId,
-        name: '默认配置',
-        bucketName: oldSettings.bucketName,
-        publicDomain: oldSettings.publicDomain || '',
-      };
+      }));
+
+      store.set('profiles', migratedProfiles);
+
+      // If there was an active ID, keep it, otherwise set the first one as active.
+      if (!store.has('activeProfileId') && migratedProfiles.length > 0) {
+          store.set('activeProfileId', migratedProfiles[0].id);
+      }
+
+      // Delete the old base settings key
+      store.delete('settings');
+
+      console.log('Migration complete. Old base settings removed.');
     }
  }
\`\`\`

</details>
<!-- 2f96d3b at https://github.com/JiQingzhe2004/R2APP/commit/2f96d3b346b3afdc4b1e3cb8b16314f763fccd8d -->

---

## 🚀 整合通知功能

本次提交主要聚焦于**整合通知功能**，为应用内通知管理引入了全新的上下文。我们不仅**更新了头部组件**以展示通知并支持清除功能，还在文件、下载、上传和设置页面中集成了通知反馈，从而**提升用户体验**。

### 🆕 **新功能**

-   **引入通知上下文**: 通过 `NotificationProvider` 和 `useNotifications` 钩子，我们为应用内通知管理建立了统一的上下文，确保通知状态在组件间正确流动。
-   **头部组件增强**: 头部组件现已支持显示通知列表，并提供**标记全部已读**和**清除所有通知**的功能，让用户可以轻松管理收到的通知。
-   **多页面集成**: 在文件、下载、上传和设置页面中集成了通知反馈，确保用户在不同操作后都能收到及时的通知提醒。

### ✨ **功能优化**

-   **通知展示优化**: 头部组件中的通知展示更加直观，支持显示通知类型（成功、错误、信息）和发送时间，让用户可以快速了解通知内容。
-   **用户体验提升**: 通过在关键操作（如切换存储桶）后添加通知反馈，用户可以更清晰地了解操作结果，提升整体使用体验。

<details>
<summary>💡 查看关键代码变更</summary>

\`\`\`diff
+import { NotificationProvider, useNotifications } from './contexts/NotificationContext';
+
+function AppContent() {
+  const { notifications, unreadCount, addNotification, markAllAsRead, clearNotifications, removeNotification } = useNotifications();
+
+  const checkStatus = useCallback(async () => {
+    // ... 其他代码 ...
+    const switchedProfile = currentProfiles.find(p => p.id === profileId);
+    if (switchedProfile) {
+        toast.success(`已切换到存储桶: ${switchedProfile.name}`);
+        addNotification({ message: `已切换到: ${switchedProfile.name}`, type: 'info' });
+    }
+  };
+
+  return (
+    <Router>
+      <Layout>
+        <Sidebar isCollapsed={isSidebarCollapsed} onToggle={toggleSidebar} />
+        <LayoutBody>
+          <Header 
+            // ... 其他属性 ...
+            notifications={notifications}
+            unreadCount={unreadCount}
+            onMarkAllRead={markAllAsRead}
+            onClearNotifications={clearNotifications}
+            onRemoveNotification={removeNotification}
+          />
+          // ... 其他代码 ...
+        </LayoutBody>
+      </Layout>
+    </Router>
+  );
+}
+
+export function Header({ 
+  // ... 其他属性 ...
+  notifications,
+  unreadCount,
+  onMarkAllRead,
+  onClearNotifications,
+  onRemoveNotification
+}) {
+  // ... 其他代码 ...
+  const [activeNotification, setActiveNotification] = useState(null);
+  const [isPopupVisible, setIsPopupVisible] = useState(false);
+  const [progress, setProgress] = useState(100);
+
+  useEffect(() => {
+    if (notifications && (!prevNotificationsRef.current || notifications.length > prevNotificationsRef.current.length)) {
+      const newest = notifications[0];
+      if (newest && newest.id !== activeNotification?.id) {
+        setActiveNotification(newest);
+      }
+    }
+    prevNotificationsRef.current = notifications;
+  }, [notifications, activeNotification];
+
+  // ... 其他代码 ...
+}
\`\`\`

</details>
<!-- c89346c at https://github.com/JiQingzhe2004/R2APP/commit/c89346c844e2c23adc30595f95d76cfe26def236 -->

---

## 🛠️ 调整主窗口尺寸并新增应用图标

本次提交主要针对应用程序的界面进行了优化，提升了视觉体验。我们调整了主窗口的尺寸，并新增了应用图标，使得整体界面更加美观和专业化。

`🆕 **新功能**`

*   **调整主窗口尺寸**: 主窗口的尺寸已从900x670调整为1200x800，提供了更宽敞的显示空间，使用户体验得到提升。
*   **新增应用图标**: 为Linux平台的应用程序新增了图标资源，增强了应用程序的可识别性和视觉吸引力。

以下是最核心的代码变更，展示了主窗口尺寸的调整和图标的应用：

<details>
<summary>💡 查看关键代码变更</summary>

\`\`\`diff
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
\`\`\`

</details>
<!-- 1a95b7b at https://github.com/JiQingzhe2004/R2APP/commit/1a95b7ba2bd850459ab94df32f6051e77315b700 -->

---

## 🚀 优化下载管理功能

本次提交对下载管理功能进行了全面的优化，重点重构了下载任务的状态管理，以支持更流畅的下载进度更新和更健壮的错误处理。同时，更新了设置获取逻辑以适应活动配置文件的需求，并清理了不再使用的预加载文件，提升了应用的整体性能和用户体验。

### 变更摘要

*   **🆕 新功能**: 引入了更细粒度的下载状态管理和进度更新机制，支持实时显示下载速度和状态变化。
*   **✨ 功能优化**: 重构了下载任务的状态管理逻辑，使其更加模块化和可扩展，同时优化了错误处理流程，提高了下载的可靠性。
*   **🐞 Bug修复**: 修复了之前版本中下载任务进度更新不及时的问题，以及在某些情况下S3客户端未正确初始化导致的下载失败问题。

通过这些改进，用户现在可以更清晰地了解下载进度，并在出现问题时获得更及时的反馈，从而获得更好的使用体验。

### 关键代码展示

<details>
<summary>💡 查看关键代码变更</summary>

\`\`\`diff
-ipcMain.on('r2-download-file', async (_, { key }) => {
+ipcMain.on('download-file', async (event, key) => {
   const s3Client = getS3Client();
   if (!s3Client) {
-    // We can't return an error directly, but we can send an event
-    // For now, we'll rely on the settings being correct.
+    mainWindow.webContents.send('download-update', { type: 'error', data: { error: 'S3 client not initialized' } });
     return;
   }
   const bucketName = getActiveSettings().bucketName;
   
   const downloadsPath = app.getPath('downloads');
   let filePath = join(downloadsPath, key);
   
   // Avoid overwriting existing files
   if (fs.existsSync(filePath)) {
     const timestamp = new Date().getTime();
     const pathData = parse(filePath);
     ...
     let downloaded = 0;
     let lastProgressTime = 0;
     let lastDownloaded = 0;
   
     Body.on('data', (chunk) => {
       downloaded += chunk.length;
       const progress = ContentLength ? Math.round((downloaded / ContentLength) * 100) : 0;
       
       const now = Date.now();
       let speed = 0;
       if (now - lastProgressTime > 500) { // Update speed every 500ms
         const timeDiff = (now - lastProgressTime) / 1000;
         const bytesDiff = downloaded - lastDownloaded;
         speed = timeDiff > 0 ? bytesDiff / timeDiff : 0;
         lastProgressTime = now;
         ...
         const currentTasks = store.get('download-tasks', {});
         if (currentTasks[taskId]) {
           currentTasks[taskId] = { ...currentTasks[taskId], progress, status: 'downloading', speed };
           store.set('download-tasks', currentTasks);
         }
         mainWindow.webContents.send('download-update', { type: 'progress', data: { id: taskId, progress, speed, status: 'downloading' } });
       });
     });
     ...
   } catch (error) {
     const errorTasks = store.get('download-tasks', {});
     if (errorTasks[taskId]) {
       errorTasks[taskId].status = 'error';
       errorTasks[taskId].error = error.message;
       store.set('download-tasks', errorTasks);
     }
     mainWindow.webContents.send('download-update', { type: 'progress', data: { id: taskId, status: 'error', error: error.message } });
   }
 });
\`\`\`

</details>
<!-- 23c5f93 at https://github.com/JiQingzhe2004/R2APP/commit/23c5f9352c9e4caea7b8dfc2ab487e7b1c75c45e -->

---

## 🚀 更新依赖项并添加应用信息功能

本次提交主要包含了对项目依赖项的升级以及一系列新功能的添加，旨在提升应用的稳定性和用户体验。

### 变更摘要

*   **🆕 **新功能**: 在主进程中新增了获取应用信息的功能，并通过IPC通信暴露给渲染进程。同时，新增了关于页面，用于展示应用的详细信息，包括名称、版本、作者和许可证信息。
*   **🛠️ **其他**: 更新了侧边栏和头部组件，以支持新添加的关于页面功能。同时，将`lucide-react`库升级到了0.525.0版本，以利用最新的图标资源。

### 关键代码展示

<details>
<summary>💡 查看关键代码变更</summary>

\`\`\`diff
+import packageJson from '../../package.json' assert { type: 'json' };
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
\`\`\`

\`\`\`diff
+import AboutPage from './pages/About';
+
+function App() {
   const [isSidebarCollapsed, setIsSidebarCollapsed] = useState(false);
   const navigate = useNavigate();
 
   return (
     <main className="flex h-[calc(100vh_-_56px)]">
       <Sidebar isCollapsed={isSidebarCollapsed} onToggle={setIsSidebarCollapsed} />
       <LayoutBody>
         <Routes>
           <Route path="/" element={<DashboardPage />} />
           <Route path="/files" element={<FilesPage />} />
           <Route path="/uploads" aname="uploads" element={<UploadsPage />} />
           <Route path="/downloads" element={<DownloadsPage />} />
           <Route path="/settings" element={<SettingsPage onSettingsSaved={refreshState} />} />
           <Route path="/about" element={<AboutPage />} />
         </Routes>
       </LayoutBody>
     </main>
   );
 }
\`\`\`

\`\`\`diff
+  { id: 'about', href: '/about', icon: Info, label: '关于应用' },
\`\`\`

</details>
<!-- a14aef5 at https://github.com/JiQingzhe2004/R2APP/commit/a14aef53658ba41cb012d6f4602a8a9192865482 -->

---

## 🚀 添加窗口控制功能

本次提交引入了完整的窗口控制机制，包括最小化、最大化和关闭窗口的功能。同时，更新了头部组件以集成这些控制按钮，并新增了黑白LOGO图标以增强界面视觉效果。这些改进将显著提升应用的用户交互体验和视觉一致性。

`🆕 **新功能**`

*   实现了窗口最小化、最大化和关闭功能，通过IPC通信实现主进程与渲染进程的交互。
*   更新头部组件，集成了窗口控制按钮，使用户可以更方便地管理窗口状态。
*   新增了黑白LOGO图标，增强了应用的视觉表现力，适应不同主题需求。

<details>
<summary>💡 查看关键代码变更</summary>

\`\`\`diff
+// IPC handlers for window controls in main/index.js
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
+});
\`\`\`

\`\`\`diff
+// Window controls in preload/index.mjs
+api.minimizeWindow: () => ipcRenderer.send('minimize-window'),
+api.maximizeWindow: () => ipcRenderer.send('maximize-window'),
+api.closeWindow: () => ipcRenderer.send('close-window'),
\`\`\`

\`\`\`diff
+// Updated Header component in header.jsx
+<Button variant="ghost" size="icon" className="h-8 w-8" onClick={() => window.api.minimizeWindow}>
+   <Minus className="h-4 w-4" />
+</Button>
+<Button variant="ghost" size="icon" className="h-8 w-8" onClick={() => window.api.maximizeWindow}>
+   <Square className="h-4 w-4" />
+</Button>
+<Button variant="ghost" size="icon" className="h-8 w-8 hover:bg-red-500/90" onClick={() => window.api.closeWindow}>
+   <X className="h-4 w-4" />
+</Button>
\`\`\`

\`\`\`diff
+// Updated Sidebar component in sidebar.jsx
+<img src={BlackLogo} alt="Logo" className="h-6 w-6 hidden dark:block" />
+<img src={WhiteLogo} alt="Logo" className="h-6 w-6 dark:hidden" />
\`\`\`
</details>
<!-- f3b89d6 at https://github.com/JiQingzhe2004/R2APP/commit/f3b89d60afd23c38540eb9f84b4f0b1af005161a -->

---

## 🚀 添加R2存储配置管理功能

本次提交主要引入了R2存储配置管理功能，支持配置文件的添加、删除和切换，同时优化了设置页面的保存逻辑，并新增了单选框组件以改善用户体验。此外，还更新了相关组件以支持新功能，确保整个应用的稳定性和易用性得到提升。

### 🆕 **新功能**

- **R2存储配置管理**: 本次变更的核心是添加了对R2存储的全面配置管理功能。用户现在可以轻松地添加、删除和切换不同的存储配置，使得数据管理更加灵活和高效。
- **数据迁移**: 为了确保旧用户能够顺利过渡到新的配置体系，我们实现了一个数据迁移工具。该工具会在应用启动时自动检测旧配置结构，并将其迁移到新的`profiles`结构中，确保数据的连续性和完整性。
- **优化设置页面**: 通过新增单选框组件和改进保存逻辑，我们显著提升了设置页面的用户体验。用户现在可以更直观地选择和保存配置，减少了操作步骤和潜在的错误。

### 关键代码展示

<details>
<summary>💡 查看关键代码变更</summary>

\`\`\`diff
// Data Migration
function runMigration() {
  const oldSettings = store.get('settings');
  // Check if old structure exists and new structure doesn't
  if (oldSettings && !store.has('profiles')) {
    console.log('Migrating old settings to new profile structure...');
    const newProfileId = uuidv4();
    const newBaseSettings = {
      accountId: oldSettings.accountId,
      accessKeyId: oldSettings.accessKeyId,
      secretAccessKey: oldSettings.secretAccessKey,
    };
    const newProfile = {
      id: newProfileId,
      name: '默认配置',
      bucketName: oldSettings.bucketName,
      publicDomain: oldSettings.publicDomain || '',
    };
    
    store.set('settings', newBaseSettings);
    store.set('profiles', [newProfile]);
    store.set('activeProfileId', newProfileId);
    console.log('Migration complete.');
  }
}

// Run migration on startup
runMigration();
\`\`\`

\`\`\`diff
// Updated IPC Handlers
ipcMain.handle('save-profiles', (event, { profiles, activeProfileId }) => {
  store.set('profiles', profiles);
  store.set('activeProfileId', activeProfileId);
  return { success: true };
});

ipcMain.handle('r2-test-connection', async (event, { settings, profile }) => {
  const testSettings = { ...settings, ...profile };
  if (!testSettings.accountId || !testSettings.accessKeyId || !testSettings.secretAccessKey || !testSettings.bucketName) {
    return { success: false, error: '缺少必要的配置信息。' }
  }
  
  const testS3Client = new S3Client({
    region: 'auto',
    endpoint: `https://${testSettings.accountId}.r2.cloudflarestorage.com`,
    credentials: {
      accessKeyId: testSettings.accessKeyId,
      secretAccessKey: testSettings.secretAccessKey,
    },
  });
  
  try {
    const command = new ListObjectsV2Command({ Bucket: testSettings.bucketName, MaxKeys: 0 });
    await testS3Client.send(command);
    return { success: true, message: '连接成功！配置信息有效。' };
  } catch (error) {
    // Handle error
  }
});
\`\`\`

</details>

通过这些关键代码片段，我们可以看到新功能的核心实现逻辑，包括数据迁移和配置管理。这些变更不仅提升了功能的完整性，还确保了应用的稳定性和用户体验。
<!-- 1eba83a at https://github.com/JiQingzhe2004/R2APP/commit/1eba83a27b518e5e1f88c4612242c7c2adc51b75 -->

---

## ✨ **功能优化**

本次提交主要围绕 **R2存储连接状态检查功能** 的添加、相关组件的更新以显示连接状态、设置页面保存功能的优化，以及 **新增Tooltip组件** 以改善用户体验。这些变更旨在提升应用的稳定性和用户交互的流畅性。

### 🆕 **新功能**
- **R2存储连接状态检查功能**: 新增了 `check-r2-status` API，用于检查R2存储的连接状态，确保数据存储的可靠性。

### ✨ **功能优化**
- **设置页面保存功能优化**: 提升了设置页面保存功能的性能和稳定性。
- **Tooltip组件新增**: 引入了 `@radix-ui/react-tooltip` 组件，改善了用户在操作界面时的提示信息展示。

### 🐞 **Bug修复**
- 修复了若干与R2存储连接状态检查相关的潜在问题。

### 关键代码展示

<details>
<summary>💡 查看关键代码变更</summary>

\`\`\`diff
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
\`\`\`

</details>

<details>
<summary>💡 查看关键代码变更</summary>

\`\`\`diff
+  checkR2Status: () => ipcRenderer.invoke('check-r2-status'),
\`\`\`

</details>
<!-- 1a7daa7 at https://github.com/JiQingzhe2004/R2APP/commit/1a7daa75a3aabaae5ff706dfaf37009fdc72eaab -->

---

## 🚀 新功能：搜索对话框功能

本次提交为应用添加了全新的搜索对话框功能，并优化了文件页面的搜索逻辑。我们调整了文件列表和搜索结果的显示方式，并改进了删除确认提示信息，以提升用户体验。

### 变更摘要

`🆕 **新功能**`

我们成功为应用引入了**搜索对话框功能**，使用户能够更方便地在文件页面中查找所需文件。这一功能不仅提升了搜索的便捷性，还优化了整体的用户体验。

- **搜索对话框的集成**: 我们在文件页面中添加了一个可交互的搜索对话框，用户可以通过输入关键词快速找到所需的文件。
- **搜索逻辑的优化**: 对搜索逻辑进行了优化，确保搜索结果的准确性和响应速度。
- **文件列表和搜索结果的显示调整**: 调整了文件列表和搜索结果的显示方式，使其更加直观和易于使用。
- **删除确认提示信息的改进**: 改进了删除确认提示信息，使用户在执行删除操作时更加谨慎，减少误操作的可能性。

### 关键代码展示

<details>
<summary>💡 查看关键代码变更</summary>

\`\`\`diff
// 在 src/App.jsx 中添加搜索对话框状态
const [isSearchDialogOpen, setIsSearchDialogOpen] = useState(false);

// 在 Header 组件中添加搜索按钮
<Header onSearchClick={() => setIsSearchDialogOpen(true)} />

// 在 FilesPage 组件中传递和更新搜索对话框状态
<Route path="/files" element={<FilesPage isSearchOpen={isSearchDialogOpen} onSearchOpenChange={setIsSearchDialogOpen} />} />
\`\`\`

</details>
<!-- 5ba7e66 at https://github.com/JiQingzhe2004/R2APP/commit/5ba7e660427fe2174b572bdefe77dd2ff51ee49f -->

---

## 🚀 文件搜索功能与依赖更新

本次提交带来了多项重要更新，旨在提升应用的易用性和功能丰富性。我们不仅引入了全新的文件搜索功能，还对现有文件列表加载逻辑进行了优化，同时改进了删除确认提示和搜索结果提示信息。此外，还更新了项目依赖项，引入了最新的UI组件库，以增强应用的现代化外观和用户体验。

### 🆕 **新功能**
- **文件搜索功能**: 引入了全新的文件搜索功能，允许用户快速定位所需文件，极大提升了工作效率。
- **搜索结果提示信息**: 优化了搜索结果的提示信息，使其更加清晰和用户友好。

### ✨ **功能优化**
- **文件列表加载逻辑**: 优化了文件列表的加载逻辑，提高了加载速度和响应性能。
- **删除确认提示**: 改进了删除确认提示，增加了用户操作的明确性，防止误操作。

### 🐞 **Bug修复**
- **依赖项更新**: 更新了项目依赖项，修复了一些潜在的bug和安全问题。

### 🆕 **新功能**
- **文件搜索功能**: 引入了全新的文件搜索功能，允许用户快速定位所需文件，极大提升了工作效率。
- **搜索结果提示信息**: 优化了搜索结果的提示信息，使其更加清晰和用户友好。

<details>
<summary>💡 查看关键代码变更</summary>

\`\`\`diff
+ipcMain.handle('r2-list-objects', async (_, { continuationToken, prefix }) => {
   const s3Client = getS3Client();
   if (!s3Client) {
     return { success: false, error: '请先在设置中配置您的存储桶。' };
   }
   const settings = store.get('settings');
 
   try {
     const command = new ListObjectsV2Command({
       Bucket: settings.bucketName,
       ContinuationToken: continuationToken,
       Prefix: prefix,
       MaxKeys: 30,
     });
     const response = await s3Client.send(command);
     return {
       success: true,
       data: {
         files: response.Contents || [],
       },
     };
   } catch (error) {
     return { success: false, error: error.message };
   }
}),
\`\`\`

</details>
<!-- aab3f96 at https://github.com/JiQingzhe2004/R2APP/commit/aab3f96c5dca6d322e3f2335f804f24269403e1a -->

---

## 🚀 更新依赖项并优化文件管理功能

本次提交带来了多项重要更新，旨在提升文件上传和下载的用户体验。我们不仅优化了核心的文件管理逻辑，还引入了全新的下载管理页面，并增强了文件类型显示。以下是本次变更的详细内容：

### 🆕 **新功能**
- **下载管理页面**: 引入了一个全新的下载管理页面，让用户可以实时监控下载任务的状态、进度，并支持手动管理（如清除已完成或删除任务）。
- **下载任务状态管理**: 实现了完整的下载任务状态管理，包括任务开始、下载中、完成和错误状态，并通过事件通知主窗口更新UI。
- **下载通知**: 通过实时进度事件，实现了下载进度的通知机制，让用户随时了解下载状态。

### ✨ **功能优化**
- **文件上传优化**: 优化了文件上传逻辑，增加了并发控制（`queueSize`）、分片上传（`partSize`）和错误处理，提升了大文件上传的稳定性和效率。
- **文件下载优化**: 改进了文件下载功能，支持断点续传和实时进度反馈，并自动处理文件名冲突问题。
- **文件页面显示逻辑**: 优化了文件页面的显示逻辑，增加了文件类型图标和描述，提升了文件的可识别性。
- **依赖项更新**: 更新了部分依赖项，引入了`uuid`库用于生成唯一的下载任务ID，并优化了路径处理功能。

### 🐞 **Bug修复**
- 修复了文件下载时可能出现的路径冲突问题，确保每个下载文件都有唯一的存储路径。
- 优化了错误处理逻辑，确保在下载失败时能够正确反馈错误信息。

### 关键代码展示

<details>
<summary>💡 查看关键代码变更</summary>

\`\`\`diff
// 文件上传优化
ipcMain.handle('r2-upload-file', async (_, { filePath, key }) => {
  // ... 省略其他代码 ...
  const upload = new Upload({
    // 新增并发控制和分片上传配置
    queueSize: 4, // optional concurrency
    partSize: 1024 * 1024 * 5, // optional size of each part
    leavePartsOnError: false, // optional manually handle dropped parts
  });
  
  // 实时进度反馈
  upload.on('httpUploadProgress', (progress) => {
    if (progress.total) {
      const percentage = Math.round((progress.loaded / progress.total) * 100);
      mainWindow.webContents.send('upload-progress', { key, percentage });
    }
  });
  // ... 省略其他代码 ...
});

// 文件下载状态管理
ipcMain.on('r2-download-file', async (_, { key }) => {
  // ... 省略其他代码 ...
  const taskId = uuidv4();
  const task = {
    id: taskId,
    key,
    filePath,
    status: 'starting',
    progress: 0,
    total: 0,
    downloaded: 0,
    createdAt: new Date().toISOString()
  };
  
  // 保存任务状态
  const currentTasks = store.get('downloads', {});
  currentTasks[taskId] = task;
  updateDownloads(currentTasks);
  
  // 实时进度监控
  Body.on('data', (chunk) => {
    task.downloaded += chunk.length;
    if (task.total > 0) {
      task.progress = Math.round((task.downloaded / task.total) * 100);
    }
    
    const now = Date.now();
    const timeDiff = (now - lastProgressTime) / 1000;
    if (timeDiff > 0.5) {
      const bytesDiff = task.downloaded - lastDownloaded;
      const speed = timeDiff > 0 ? bytesDiff / timeDiff : 0;
      lastDownloaded = task.downloaded;
      lastProgressTime = now;
      
      const tasks = store.get('downloads', {});
      tasks[taskId] = { ...tasks[taskId], ...task, speed };
      updateDownloads(tasks);
      mainWindow.webContents.send('download-progress', { id: taskId, progress: task.progress, speed: speed, status: 'downloading' });
    }
  });
  // ... 省略其他代码 ...
});
\`\`\`

</details>
<!-- ca00387 at https://github.com/JiQingzhe2004/R2APP/commit/ca00387ae115afc12e8c76c3554ff54675a9b43b -->

---

## 🚀 依赖项更新与功能增强

本次提交带来了多项重要的更新和功能增强，旨在提升用户体验和应用的稳定性。我们引入了新的依赖项 `sonner` 用于通知系统，增强了快捷键支持，改进了侧边栏的折叠功能，并优化了文件页面的加载逻辑。以下是本次变更的详细说明：

### 🆕 **新功能**
- **添加 `sonner` 库**: 引入 `sonner` 用于在设置页面中提供更友好的 Toast 通知，以反馈连接和保存状态。
- **注册 F5 快捷键**: 在主进程中注册 F5 快捷键，用于刷新窗口，提升操作便捷性。

### ✨ **功能优化**
- **侧边栏折叠功能改进**: 优化了侧边栏的折叠逻辑，使其更加平滑和用户友好。
- **文件页面加载和显示逻辑优化**: 改进了文件页面的加载和显示逻辑，提升了性能和响应速度。

### 🐞 **Bug修复**
- 无明确 Bug 修复记录，但重构和优化有助于提升代码稳定性。

### 关键代码展示

<details>
<summary>💡 查看关键代码变更</summary>

\`\`\`diff
+import { globalShortcut } from 'electron'
+
+app.whenReady().then(() => {
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
+
+app.on('will-quit', () => {
+  // Unregister all shortcuts.
+  globalShortcut.unregisterAll();
+});
+
 app.on('window-all-closed', () => {
   if (process.platform !== 'darwin') {
     app.quit()
   }
 })
\`\`\`

\`\`\`diff
+import { Toaster } from 'sonner';
+
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
\`\`\`

</details>
<!-- 367d89f at https://github.com/JiQingzhe2004/R2APP/commit/367d89f63d2af19eba08e01d7fb1b23ed5490c6f -->

---

## 🚀 **修复构建后无法运行的问题**

本次提交针对 R2 存储资源管理器桌面应用进行了关键修复，解决了构建后无法正常运行的问题。这是一个重要的Bug修复，确保用户在开发环境外也能顺利使用应用。

### ✨ **功能优化**

*   **Bug修复**: 修复了应用在构建后（非开发模式）无法启动的严重问题。通过增强调试日志、优化资源路径检查以及正确配置 `electron-serve`，确保了生产环境下的稳定运行。
*   **内部重构**: 对主进程的启动逻辑和资源加载方式进行了调整，特别是针对 `dist` 目录的检测和 `electron-serve` 的集成进行了优化，使其能正确处理构建后的文件结构。

应用现在能够在开发模式（`npm run dev`）和生产模式（`npm run build:win` / `mac` / `linux`）下均能正常启动和运行，提升了用户体验和应用的健壮性。

由于本次变更主要涉及内部逻辑和构建流程的修复，并未添加新功能或修改用户界面，因此不包含关键代码展示。

```bash
npm run dev
# 或
npm run build:win
# 或
npm run build:mac
# 或
npm run build:linux
```
<!-- 860c023 at https://github.com/JiQingzhe2004/R2APP/commit/860c023f2ccd8321c602da0d7cf5a28014ffb378 -->