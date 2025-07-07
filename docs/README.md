# CS-Explorer应用更新说明

## 🗑️ 清理不必要的文件

本次提交专注于对项目中的`.gitignore`文件进行精简，移除了若干已不再需要的条目。此举旨在**提升`.gitignore`文件的可读性**，并确保**仓库中不包含任何无用的文件**，从而**保持仓库的整洁和高效**。

### 变更分类
- `🗑️ 清理工作`

### 详细说明
通过移除以下条目，我们确保了`.gitignore`文件更加**聚焦于真正需要忽略的文件和目录**：

- `node_modules`：虽然`node_modules`通常被忽略，但根据项目具体情况，此条目可能需要保留。
- `.vscode`：如果项目不再使用VS Code工作区，此条目可安全移除。
- `out`、`dist`、`release`：这些目录通常包含构建输出，根据项目构建流程，可能不再需要忽略。
- 日志文件：`npm-debug.log*`、`yarn-debug.log*`、`yarn-error.log*`，如果项目不再需要忽略这些日志文件，可移除。
- `dist-electron`：如果项目不再使用Electron构建输出，此条目可安全移除。
- 图标文件：`resources/icon.ico`，如果项目不再使用此图标文件，可移除。
- 临时文件：`src/version.json`，如果项目不再需要忽略此文件，可移除。

通过这些清理工作，我们确保了`.gitignore`文件更加**精准和高效**，从而**提升项目的整体可维护性**。

### 关键代码修改
```diff
-node_modules
-.vscode
-out
-dist
-release
-
-# Log files
-npm-debug.log*
-yarn-debug.log*
-yarn-error.log*
-
-# Build output
-dist-electron
-
-# icon
-resources/icon.ico
-
-# temp file
-src/version.json
```
<!-- 2d53ce8 at https://github.com/JiQingzhe2004/R2APP/commit/2d53ce8db3d3bd95c41d4a866ce9de00b619ea2e -->

---

## ✨ 功能优化

本次提交专注于提升应用的导航体验和信息透明度，通过引入更新日志页面并优化侧边栏布局，为用户提供了更便捷的访问路径。以下是本次变更的详细内容：

### 变更摘要

我们成功为应用添加了一个全新的**更新日志页面**，让用户能够轻松获取最新的版本信息。同时，我们对侧边栏进行了更新，新增了指向该页面的链接，并微调了主应用布局以提升整体视觉效果和用户体验。

#### 具体变更内容：

*   **🆕 新功能** - 新增了 `ReleaseNotesPage` 组件，用于展示应用的更新日志。
*   **🆕 新功能** - 在侧边栏菜单中添加了“更新日志”的导航项，并使用了 `ScrollText` 图标进行可视化标识。
*   **✨ 功能优化** - 优化了主应用布局，使整体结构更加清晰。

### 关键代码展示

#### `App.jsx` - 添加新页面路由

```jsx
import ReleaseNotesPage from './pages/ReleaseNotes';

function AppContent() {
  // ... 省略其他代码 ...

  <Routes>
    // ... 省略其他路由 ...
    <Route path="/releasenotes" element={<ReleaseNotesPage />} />
  </Routes>
}
```

#### `sidebar.jsx` - 更新侧边栏菜单

```jsx
export function Sidebar({ isCollapsed, onToggle }) {
  // ... 省略其他代码 ...

  const sidebarLinks = [
    // ... 省略其他链接 ...
    {
      id: 'releasenotes',
      href: '/releasenotes',
      icon: ScrollText,
      label: '更新日志',
    },
  ];

  // ... 省略其他代码 ...
}
```

#### `ReleaseNotesPage.jsx` - 新增页面组件

```jsx
import React from 'react';

const ReleaseNotesPage = () => {
  const releaseNotesUrl = "https://jiqingzhe2004.github.io/";

  return (
    <div className="absolute inset-0">
      <iframe
        src={releaseNotesUrl}
        title="更新日志"
        className="w-full h-full border-0"
      />
    </div>
  );
};

export default ReleaseNotesPage;
```

通过这些变更，我们不仅丰富了应用的功能，还提升了用户对版本更新的关注度和获取信息的便捷性。
<!-- 57a9b91 at https://github.com/JiQingzhe2004/R2APP/commit/57a9b9191f00267ef459c933b0df1f421e7051a7 -->

---

## 📜 添加项目许可证

### 变更摘要

本次提交为项目添加了必要的许可证文件，确保项目的法律合规性并明确代码的使用权限。这是一个基础但至关重要的步骤，它为项目的使用者和贡献者提供了清晰的指导。

**分类**: `🆕 新功能`

许可证文件采用了 **MIT License**，这是一种非常宽松的开源许可证，允许使用者自由地使用、修改和分发代码，只需满足在代码中包含原始版权声明和许可证声明的条件。这种许可证极大地促进了代码的共享和再利用，有助于项目的推广和社区的发展。

以下是新添加的许可证文件的关键部分：

```markdown
MIT License

Copyright (c) 2025 Forrest

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
<!-- 070eaa3 at https://github.com/JiQingzhe2004/R2APP/commit/070eaa3de84fa03b7245cb6f7707a1ff8d26d24c -->

---

## 🛠️ 更新项目配置与版本管理

本次提交主要针对项目的配置和版本管理进行了全面升级，旨在提升构建流程的自动化程度和用户体验。通过以下关键变更，我们实现了版本信息的自动化注入和展示：

### 变更摘要

*   **更新 `.gitignore` 文件** (`🆕 新功能`):
    *   排除了日志文件 (`npm-debug.log*`, `yarn-debug.log*`, `yarn-error.log*`) 和构建输出文件 (`dist-electron`, `dist`, `release`)，确保代码仓库的整洁。
    *   添加了对图标文件 (`resources/icon.ico`) 和临时版本文件 (`src/version.json`) 的排除，优化仓库结构。
    *   ```markdown
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
        ```

*   **修改 `package.json` 中的构建脚本** (`✨ 功能优化`):
    *   在 `dev` 和 `build` 脚本执行前，通过注入 `inject-version.cjs` 脚本自动生成并注入版本信息，简化了构建流程。
    *   ```markdown
        - "dev": "electron-vite dev",
        - "build": "electron-vite build",
        + "dev": "node ./scripts/inject-version.cjs && electron-vite dev",
        + "build": "node ./scripts/inject-version.cjs && electron-vite build",
        ```

*   **新增 `inject-version.cjs` 脚本** (`🆕 新功能`):
    *   该脚本负责从环境变量 `VERSION` 获取版本号，若无则自动生成开发版本号（格式为 `dev-YYYY-MM-DDTHH:mm:ss.sssZ`）。
    *   将版本信息写入 `src/version.json` 文件，供前端代码引用。
    *   ```markdown
        const fs = require('fs');
        const path = require('path');
        
        // Get version from environment variable, or generate a dev version
        const version = process.env.VERSION || `dev-${new Date().toISOString()}`;
        
        const versionData = {
          version: version,
        };
        
        // The path to write the version file to.
        // We write it inside `src` so it's easily importable by the frontend code.
        const outputPath = path.join(__dirname, '../src/version.json');
        
        // Write the version data to the file.
        fs.writeFileSync(outputPath, JSON.stringify(versionData, null, 2));
        
        console.log(`Version ${version} injected into ${outputPath}`);
        ```

*   **在 About 页面中显示应用版本信息** (`✨ 功能优化`):
    *   修改了 `src/pages/About.jsx`，引入 `versionData` 并展示应用版本信息。
    *   优化了 About 页面的用户界面，添加了应用 Logo 和 GitHub Issue 链接，提升了用户体验。
    *   ```markdown
        +import { useTheme } from '@/components/theme-provider';
        +import versionData from '@/version.json';
        
        export default function AboutPage() {
        +  const { theme } = useTheme();
            const [appInfo, setAppInfo] = useState({
              name: 'R2 存储管理器',
              version: '...',
            });
        
            // ... (rest of the code)
        
            +<div className="text-center mt-6 text-xs text-muted-foreground space-y-2">
            +   <div className="flex items-center justify-center gap-x-4">
            +      <span>版本: {versionData.version}</span>
            +      <div className="h-3 w-px bg-border" />
            +      <a 
            +        href={appInfo.githubUrl ? `${appInfo.githubUrl}/issues` : "#"}
            +        target="_blank" 
            +        rel="noopener noreferrer"
            +        className="flex items-center gap-1 hover:text-primary transition-colors"
            +      >
            +        <Github size={12} />
            +        <span>提交 Issue</span>
            +      </a>
            +  </div>
            +  <p>
            +    Copyright © {new Date().getFullYear()} {appInfo.author}. All Rights Reserved.
            +  </p>
            +</div>
            +
            <div>
              // ... (rest of the code)
            </div>
          }
        }
        ```

通过这些变更，我们不仅优化了项目的构建流程，还提升了用户对应用版本信息的感知，使版本管理更加透明和自动化。
<!-- 100329b at https://github.com/JiQingzhe2004/R2APP/commit/100329be787efa753a624b7c6ecb241f6d5c1e8b -->

---

## 🚀 v3.0.0

本次更新带来了令人兴奋的新功能和用户体验优化，标志着 `CS-Explorer` 应用程序的全新飞跃。我们不仅提升了界面的交互性，还解决了用户在代码管理中遇到的一些痛点。以下是本次发布的详细变更：

### ✨ 功能优化

*   **增强代码分享体验**: 在文件预览组件中，我们新增了**复制代码到剪贴板**的功能。这一改进极大地简化了用户分享代码片段的过程，让协作变得更加高效和便捷。
*   **界面交互性提升**: 引入了 `Copy` 图标，不仅美化了界面，还为用户提供了直观的操作提示，使得代码预览区域的交互更加友好。

### 🆕 新功能

*   **代码复制功能**: 通过点击新增的 `Copy` 图标，用户可以轻松地将代码内容复制到剪贴板，无需打开新的应用程序或进行繁琐的复制操作。这一功能对于开发者来说尤其有用，可以快速地在不同的编辑器或平台之间传递代码。

### 关键代码展示

```jsx
import { Copy } from 'lucide-react';
import { toast } from 'sonner';

const handleCopy = () => {
  if (content) {
    navigator.clipboard.writeText(content);
    toast.success('代码已复制到剪贴板');
  }
};

const FilePreview = ({ file, publicUrl, open, onOpenChange }) => {
  // ... 其他代码 ...

  if (isCode(fileName)) {
    return (
      <div className="relative">
        <Button
          variant="ghost"
          size="icon"
          className="absolute top-2 right-2 h-7 w-7"
          onClick={handleCopy}
        >
          <Copy className="h-4 w-4" />
        </Button>
        <SyntaxHighlighter language={fileName.split('.').pop()} style={atomDark} showLineNumbers>
          {content}
        </SyntaxHighlighter>
      </div>
    );
  }
};
```

通过这些改进，`CS-Explorer` 现在不仅功能更加强大，而且用户体验也得到了显著提升。我们相信，这些更新将为用户带来更加流畅和高效的工作流程。
<!-- 1031df0 at https://github.com/JiQingzhe2004/R2APP/commit/1031df01689f39efdfa178fa0b5a117fdc303d35 -->

---

## ✨ 功能优化

本次提交为应用程序引入了强大的文件预览功能，极大地提升了用户体验。现在用户可以直接在文件页面中预览代码和图片文件，无需跳转到其他工具或平台。此外，我们还集成了文件预览组件，并对依赖项进行了更新，引入了`react-syntax-highlighter`库以支持代码高亮显示，使得代码预览更加专业和易读。

### 🆕 新功能

- **文件预览功能**: 支持代码和图片文件的预览，用户可以直接在应用内查看文件内容。
- **文件预览组件集成**: 在文件页面中集成了文件预览组件，使用户体验更加流畅和直观。
- **代码高亮显示**: 更新依赖项，添加`react-syntax-highlighter`以支持代码高亮显示，提升代码预览的专业性。

### 关键代码

```javascript
// electron/main/index.js
const PREVIEW_FILE_SIZE_LIMIT = 1024 * 1024; // 1MB

ipcMain.handle('get-object-content', async (event, key) => {
  const storage = await getStorageClient();
  if (!storage) {
    return { success: false, error: '未找到有效的存储配置' };
  }
  const { client, type, bucket } = storage;

  try {
    let content = '';
    let fileTooLarge = false;

    if (type === 'r2') {
      const command = new GetObjectCommand({ Bucket: bucket, Key: key });
      const response = await client.send(command);

      if (response.ContentLength > PREVIEW_FILE_SIZE_LIMIT) {
        fileTooLarge = true;
      } else {
        content = await response.Body.transformToString();
      }
    } else if (type === 'oss') {
      const response = await client.get(key);
      if (response.res.size > PREVIEW_FILE_SIZE_LIMIT) {
        fileTooLarge = true;
      } else {
        content = response.content.toString('utf-8');
      }
    }

    if (fileTooLarge) {
      return { success: false, error: '文件过大，无法预览。' };
    }

    return { success: true, content };
  } catch (error) {
    console.error(`Failed to get content for ${key}:`, error);
    return { success: false, error: `获取文件内容失败: ${error.message}` };
  }
});
```

通过这些变更，我们不仅增强了应用的功能性，还优化了用户体验，使得文件预览更加便捷和高效。
<!-- 71f832c at https://github.com/JiQingzhe2004/R2APP/commit/71f832c295634a85e78416bb7113b82450071990 -->

---

## 🚀 新增文件夹管理功能

### 变更摘要

本次提交带来了文件夹管理功能的全面升级，让文件的组织和操作更加灵活高效。我们不仅实现了创建和删除文件夹的核心功能，还对文件列表显示进行了优化，现在能够清晰地区分文件夹和文件。此外，文件上传逻辑也得到了改进，现在支持选择文件夹进行上传，极大地提升了用户体验。

#### 功能分类
- `🆕 新功能`: 文件夹的创建与删除
- `✨ 功能优化`: 文件列表显示，区分文件夹与文件
- `✨ 功能优化`: 文件上传逻辑，支持选择文件夹上传
- `🐞 Bug修复`: 文件删除逻辑，支持文件夹的删除操作
- `✨ 功能优化`: 更新依赖项，引入 `@radix-ui/react-separator` 增强UI效果

### 关键代码展示

#### 文件夹和文件列表显示优化
```javascript
// ListObjectsV2Command 参数更新，增加 Delimiter 参数
const command = new ListObjectsV2Command({
  Bucket: storage.bucket,
  ContinuationToken: continuationToken,
  Prefix: prefix,
  Delimiter: '/',
  MaxKeys: 50,
});

// 处理响应，区分文件夹和文件
let folders = (response.CommonPrefixes || []).map(p => ({
  key: p.Prefix,
  type: 'folder'
}));
let files = (response.Contents || []).map(f => ({
  key: f.Key,
  lastModified: f.LastModified,
  size: f.Size,
  etag: f.ETag
}));

// 合并并排序，文件夹在前
const combined = [
  ...folders.map(f => ({ ...f, isFolder: true })),
  ...files.map(f => ({ ...f, isFolder: false }))
].filter(item => item.key !== prefix);
```

#### 文件夹删除逻辑
```javascript
// delete-folder 事件处理
ipcMain.handle('delete-folder', async (event, prefix) => {
  const storage = await getStorageClient();
  if (!storage) {
    return { success: false, error: '未找到有效的存储配置' };
  }
  const { client, type, bucket } = storage;

  try {
    let allKeys = [];
    if (type === 'r2') {
      // 处理AWS S3的文件夹删除
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
    } else if (type === 'oss') {
      // 处理OSS的文件夹删除
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
    }

    // 批量删除文件
    if (allKeys.length > 0) {
      if (type === 'r2') {
        for (let i = 0; i < allKeys.length; i += 1000) {
          const chunk = allKeys.slice(i, i + 1000);
          await client.send(new DeleteObjectsCommand({
            Bucket: bucket,
            Delete: { Objects: chunk.map(k => ({ Key: k })) },
          }));
        }
      } else if (type === 'oss') {
        await client.deleteMulti(allKeys, { quiet: true });
      }
    }

    return { success: true, deletedCount: allKeys.length };
  } catch (error) {
    return { success: false, error: error.message };
  }
});
```

这些关键代码片段展示了如何通过更新 `ListObjectsV2Command` 参数来区分文件夹和文件，以及如何实现文件夹的批量删除逻辑。这些改进不仅提升了功能的完整性，还增强了用户操作的便捷性和准确性。
<!-- ccb3eac at https://github.com/JiQingzhe2004/R2APP/commit/ccb3eac0c6a69e41794be4ea9f59056bc31051f5 -->

---

## 🚀 v2.0.1

本次更新为CS-Explorer带来了令人兴奋的变革，不仅升级了版本，还引入了多项新功能与优化，旨在提升用户体验和操作效率。以下是本次更新的详细内容：

### ✨ 功能优化

- **仪表盘存储使用情况展示**：现在仪表盘将直观显示存储使用情况，让用户轻松掌握空间占用。
- **仪表盘最近活动记录**：仪表盘新增最近活动记录功能，清晰展示上传、下载和删除操作的历史。
- **设置页面存储配额配置**：设置页面现已支持存储配额配置，用户可以根据需求灵活调整存储限制。

### 🆕 新功能

- **最近活动记录功能**：新增了最近活动记录功能，支持记录上传、下载和删除操作，让用户随时掌握文件变动。
- **窗口最大化状态监听**：增强了窗口控制功能，现在可以监听窗口最大化状态的变化，提供更流畅的操作体验。

### 🐞 Bug修复

- **存储桶统计信息获取优化**：修复了获取存储桶统计信息时的一些潜在问题，确保数据准确性。
- **文件删除操作优化**：优化了文件删除操作的流程，提升了删除效率和用户体验。

### 代码亮点

以下是一些关键代码节选，展示了本次更新的核心改动：

```javascript
// 添加最近活动记录功能
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
ipcMain.handle('get-bucket-stats', async () => {
  const storage = await getStorageClient();
  if (!storage) {
    return { success: false, error: '未找到活动的存储配置' };
  }
  const activeProfile = getActiveProfile();
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
    return { success: true, data: { 
      totalCount, 
      totalSize, 
      bucketName: storage.bucket,
      storageQuotaGB: !isNaN(quota) && quota > 0 ? quota : 10
    } };
  } catch (error) {
    console.error('Failed to get bucket stats:', error);
    return { success: false, error: error.message };
  }
});
```

通过这些改动，CS-Explorer 2.0.1版本将为您带来更高效、更便捷的操作体验。欢迎尝试并分享您的反馈！
<!-- 48117cc at https://github.com/JiQingzhe2004/R2APP/commit/48117cc0f853359c74720768918932d9ac241033 -->

---

## 🆕 v2.0.1

本次更新带来了多项改进和优化，旨在提升用户体验和应用的整体质量。以下是本次版本的主要变更内容：

### ✨ 功能优化
我们深入优化了头部组件的配置选择功能，引入了单选框来替代原有的下拉菜单项。这一改变不仅使用户在切换配置时更加直观，也显著提升了界面的整洁度和操作的便捷性。具体实现如下：

```jsx
<DropdownMenuRadioGroup value={activeProfileId} onValueChange={onProfileSwitch}>
  {profiles.map(profile => (
    <DropdownMenuRadioItem key={profile.id} value={profile.id}>
      {profile.name}
    </DropdownMenuRadioItem>
  ))}
</DropdownMenuRadioGroup>
```

此外，我们还调整了文件页面的文件名显示方式，增加了截断效果，以适应更长的文件名并避免界面混乱。这一改动确保了即使在文件名较长的情况下，用户也能清晰地看到文件名，而不会因为过长的文本而遮挡其他重要信息。

```jsx
<TableCell className="font-medium max-w-xs truncate" title={key}>
  {key}
</TableCell>
```

### 🐞 Bug修复
在关于页面，我们更新了GitHub链接，确保用户能够正确访问到项目的官方仓库。

```jsx
githubUrl: 'https://github.com/JiQingzhe2004/R2APP'
```

### 其他
我们还对下拉菜单的指示器进行了微调，提升了视觉上的清晰度和美观度。

```jsx
<Check className="h-4 w-4" />
```

通过这些细致的调整和优化，`v2.0.1` 版本不仅增强了功能的易用性，还提升了整体的用户体验。我们相信这些改进将为您带来更加流畅和愉悦的使用感受。
<!-- d3ac191 at https://github.com/JiQingzhe2004/R2APP/commit/d3ac1915e8beaf963eb4ce3df2e89345e945eafd -->

---

## ✨ 功能优化

本次提交主要对应用进行了全面的升级和优化，旨在提升用户体验和视觉效果。以下是本次变更的详细内容：

### 变更摘要

*   **应用名称和版本更新**: 我们已经将应用名称从 `r2-explorer` 更改为 `CS-Explorer`，并将版本号从 `1.0.0` 升级到 `2.0.0`。这一变更反映了应用功能的扩展，现在它不仅支持管理Cloudflare R2存储，还扩展到了支持在线云存储的管理。
*   **描述优化**: 应用描述也进行了相应的更新，从 "一个用于管理Cloudflare R2存储的现代化桌面应用。" 修改为 "一个用于管理在线云存储的现代化桌面应用。"，更准确地描述了应用的新功能和目标用户。
*   **视觉提升**: 此外，我们还替换了应用图标和LOGO，以提升整体视觉效果，使应用更具吸引力。

### 分类和图标

*   `✨ 功能优化`: 应用名称和版本的更新，描述的优化，以及图标和LOGO的替换，都是为了提升用户体验和视觉效果，属于功能优化的范畴。

### 关键代码

以下是最关键的代码修改，展示了应用名称和版本的更新：

```json
{
-  "name": "r2-explorer",
-  "version": "1.0.0",
-  "description": "一个用于管理Cloudflare R2存储的现代化桌面应用。",
+  "name": "CS-Explorer",
+  "version": "2.0.0",
+  "description": "一个用于管理在线云存储的现代化桌面应用。",
   "main": "out/main/index.js",
   "author": "吉庆喆",
   "license": "MIT"
}
```

通过这些修改，我们相信用户将能享受到更现代化、更易用的应用体验。
<!-- 8027d10 at https://github.com/JiQingzhe2004/R2APP/commit/8027d10dce10e71d206c7c772c34ffeb98ad8d3c -->

---

## 🚀 添加阿里云OSS支持

### 变更摘要

本次提交为应用带来了** 🆕 新功能 **：对阿里云OSS（对象存储服务）的全栈支持。我们不仅引入了 `ali-oss` 依赖以构建OSS交互模块，还进行了深度的系统重构，以优雅地处理不同存储类型（目前主要支持 R2）的文件操作。此外，我们还对设置页面进行了** ✨ 功能优化 **，使其能够无缝地添加和管理OSS配置，显著提升了用户体验。

#### 核心变更点

- **引入 `ali-oss` 依赖**: 通过在 `electron.vite.config.js` 中添加 `ali-oss` 到 `external` 列表，确保了OSS SDK能够被正确加载和使用。
- **重构文件处理逻辑**: 在 `electron/main/index.js` 中，我们移除了旧的调试日志输出，并引入了基于 `ali-oss` 的连接测试逻辑。这使得应用能够根据配置类型（如 R2）动态选择正确的存储客户端和认证方式。
- **增强设置页面功能**: 同样在 `electron/main/index.js` 中，我们对配置迁移和保存逻辑进行了优化，确保旧版设置能够平滑迁移到新的配置结构中，并支持通过设置页面直接管理OSS相关的配置项。

#### 关键代码展示

```javascript
// electron.vite.config.js
export default defineConfig({
  // ... 其他配置
  external: ['@electron-toolkit/utils', 'electron-store', 'ali-oss']
});

// electron/main/index.js
// 引入阿里云OSS SDK
import OSS from 'ali-oss';

// 测试连接函数
ipcMain.handle('test-connection', async (event, profile) => {
  if (profile.type === 'r2') {
    if (!profile.accountId || !profile.accessKeyId || !profile.secretAccessKey || !profile.bucketName) {
      return { success: false, error: '缺少 R2 配置信息。' }
    }
    const testS3Client = new S3Client({
      region: 'auto',
      endpoint: `https://${...}`
    });
    // ... 连接测试逻辑
  }
});
```

通过这些改动，用户现在可以轻松地通过设置页面配置并测试其阿里云OSS账户，确保文件操作能够稳定运行。这一功能的加入不仅扩展了应用的适用范围，也为用户提供了更多灵活的存储选择。
<!-- 2f96d3b at https://github.com/JiQingzhe2004/R2APP/commit/2f96d3b346b3afdc4b1e3cb8b16314f763fccd8d -->

---

## 🚀 整合通知功能

### 变更摘要

本次提交实现了应用内通知系统的全面整合，为用户带来了更流畅、及时的信息反馈体验。我们引入了通知上下文管理，确保通知在应用各环节得到有效处理。同时，对头部组件进行了重大更新，使其不仅能够显示通知，还支持用户清除通知的功能。此外，在文件、下载、上传和设置页面中集成了通知反馈机制，显著提升了用户体验。

**变更分类**:
- `🆕 新功能`: 新增通知上下文管理与应用内通知集成。
- `✨ 功能优化`: 更新头部组件以支持显示和清除通知。
- `✨ 功能优化`: 在多个页面集成通知反馈，提升用户体验。

### 关键代码展示

```javascript
// src/App.jsx
import { NotificationProvider, useNotifications } from './contexts/NotificationContext';

function AppContent() {
  const { notifications, unreadCount, addNotification, markAllAsRead, clearNotifications, removeNotification } = useNotifications();

  const handleProfileSwitch = async (profileId) => {
    // ... 现在通知用户已切换到新存储桶
    const switchedProfile = currentProfiles.find(p => p.id === profileId);
    if (switchedProfile) {
        toast.success(`已切换到存储桶: ${switchedProfile.name}`);
        addNotification({ message: `已切换到: ${switchedProfile.name}`, type: 'info' });
    }
  };

  return (
    <Router>
      <Layout>
        <Sidebar isCollapsed={isSidebarCollapsed} onToggle={toggleSidebar} />
        <LayoutBody>
          <Header 
            // ... 其他属性
            notifications={notifications}
            unreadCount={unreadCount}
            onMarkAllRead={markAllAsRead}
            onClearNotifications={clearNotifications}
            onRemoveNotification={removeNotification}
          />
          {/* ... 其他内容 */}
        </LayoutBody>
      </Layout>
    </Router>
  );
}
```

```javascript
// src/components/header.jsx
import { Bell, TextSearch, ShieldEllipsis, ShieldCheck, ShieldX, ChevronsUpDown, Minus, Square, X, CheckCircle, XCircle, Trash2, Info } from 'lucide-react';

export function Header({ 
  // ... 其他属性
  notifications,
  unreadCount,
  onMarkAllRead,
  onClearNotifications,
  onRemoveNotification
}) {
  const [activeNotification, setActiveNotification] = useState(null);
  const [isPopupVisible, setIsPopupVisible] = useState(false);

  useEffect(() => {
    if (notifications && (!prevNotificationsRef.current || notifications.length > prevNotificationsRef.current.length)) {
      const newest = notifications[0];
      if (newest && newest.id !== activeNotification?.id) {
        setActiveNotification(newest);
      }
    }
    prevNotificationsRef.current = notifications;
  }, [notifications, activeNotification]);

  // ... 其他逻辑

  return (
    <>
      {/* ... 其他内容 */}
      <Bell className="h-5 w-5 cursor-pointer" onClick={() => setIsPopupVisible(!isPopupVisible)} />
      {isPopupVisible && (
        <Card className="absolute right-4 top-16 w-64 bg-white shadow-lg rounded-md overflow-hidden">
          <Card.Header>
            <Card.Title className="text-lg font-semibold">通知</Card.Title>
            <Card.Description>您有 {unreadCount} 条未读通知</Card.Description>
          </Card.Header>
          <Card.Body>
            {notifications.map(notification => (
              <div key={notification.id} className="flex items-center p-2 hover:bg-gray-100">
                <NotificationIcon type={notification.type} />
                <span className="ml-2">{notification.message}</span>
              </div>
            ))}
          </Card.Body>
          <Card.Footer>
            <Button onClick={onMarkAllRead}>全部标为已读</Button>
            <Button onClick={onClearNotifications} className="ml-2">清除所有通知</Button>
          </Card.Footer>
        </Card>
      )}
    </>
  );
}
```

这些代码片段展示了如何在应用中集成通知上下文管理，以及如何在头部组件中显示和清除通知。通过这些更新，用户现在可以在应用中更方便地接收和处理通知，从而获得更好的使用体验。
<!-- c89346c at https://github.com/JiQingzhe2004/R2APP/commit/c89346c844e2c23adc30595f95d76cfe26def236 -->

---

## 🛠️ 调整主窗口尺寸及添加应用图标

本次提交主要针对应用的界面进行了优化，调整了主窗口的尺寸并新增了应用图标，旨在提升整体视觉体验和应用的专业感。

### 变更摘要

*   **调整主窗口尺寸**: 主窗口的尺寸已从 `900x670` 调整为 `1200x800`。这一改变将提供更宽敞的工作空间，使用户在多任务处理和信息浏览时拥有更佳的体验。
*   **新增应用图标**: 为应用程序添加了图标资源，特别是在 Linux 平台上。这一改进将使应用在任务栏和 dock 中更加突出，增强品牌识别度，并使界面更加完整和专业。

这些调整属于 `✨ 功能优化` 类别，旨在通过提升视觉一致性和界面美观度来增强用户满意度。

### 关键代码展示

```javascript
mainWindow = new BrowserWindow({
  width: 1200,
  height: 800,
  // ... 其他配置
  ...(process.platform === 'linux' ? {} : { icon: join(__dirname, '../../resources/icon.ico') }),
  // ... 其他配置
});
```

通过上述代码中的修改，我们不仅调整了窗口尺寸，还在非 Linux 平台上集成了应用图标，从而显著提升了应用的视觉效果和用户体验。
<!-- 1a95b7b at https://github.com/JiQingzhe2004/R2APP/commit/1a95b7ba2bd850459ab94df32f6051e77315b700 -->

---

## 🛠️ 优化下载管理功能

本次提交对下载管理功能进行了全面优化，重点重构了下载任务的状态管理，以支持更精细的下载进度更新和错误处理。同时，更新了设置获取逻辑以适应活动配置文件的需求，并清理了不再使用的预加载文件，提升了应用的整洁性和性能。

### 🆕 新功能
- **下载进度与错误处理**: 引入了实时下载进度更新和详细的错误处理机制，确保用户在下载过程中获得更清晰的反馈和问题追踪。
- **活动配置文件支持**: 优化了设置获取逻辑，使其能够根据当前活动配置文件动态调整下载行为，增强了应用的灵活性。

### ✨ 功能优化
- **状态管理重构**: 对下载任务的状态管理进行了重构，采用更现代化的数据存储和更新方式，提高了数据一致性和处理效率。
- **文件冲突处理**: 在下载文件前检查目标路径是否已存在文件，如存在则自动添加时间戳后缀，避免覆盖用户现有文件，提升了用户体验。

### 🐞 Bug修复
- **S3客户端初始化问题**: 修复了S3客户端未初始化时无法正确处理错误的问题，确保在客户端未准备好时能够向用户显示明确的错误信息。
- **文件流错误处理**: 改进了文件流错误处理机制，确保在下载过程中出现的任何错误都能被捕获并正确反馈给用户。

#### 关键代码示例

```javascript
// 优化后的下载任务处理逻辑
ipcMain.on('download-file', async (event, key) => {
  const s3Client = getS3Client();
  if (!s3Client) {
    mainWindow.webContents.send('download-update', { type: 'error', data: { error: 'S3 client not initialized' } });
    return;
  }
  
  const bucketName = getActiveSettings().bucketName;
  const downloadsPath = app.getPath('downloads');
  let filePath = join(downloadsPath, key);
  
  if (fs.existsSync(filePath)) {
    const timestamp = new Date().getTime();
    const pathData = parse(filePath);
    filePath += `-${timestamp}`;
  }
  
  const task = {
    filePath,
    status: 'starting',
    progress: 0,
    createdAt: new Date().toISOString(),
  };
  
  const tasks = store.get('download-tasks', {});
  tasks[task.id] = task;
  store.set('download-tasks', tasks);
  
  mainWindow.webContents.send('download-update', { type: 'start', task });
  
  try {
    const command = new GetObjectCommand({ Bucket: bucketName, Key: key });
    const { Body, ContentLength } = await s3Client.send(command);
    
    if (!Body) {
      throw new Error('Could not get file body from S3');
    }
    
    const fileStream = fs.createWriteStream(filePath);
    let downloaded = 0;
    let lastProgressTime = 0;
    
    Body.on('data', (chunk) => {
      downloaded += chunk.length;
      const progress = ContentLength ? Math.round((downloaded / ContentLength) * 100) : 0;
      
      const now = Date.now();
      if (now - lastProgressTime > 500) {
        const speed = (downloaded - lastDownloaded) / ((now - lastProgressTime) / 1000);
        lastProgressTime = now;
        lastDownloaded = downloaded;
      }
      
      const currentTasks = store.get('download-tasks', {});
      if (currentTasks[task.id]) {
        currentTasks[task.id] = { ...currentTasks[task.id], progress, status: 'downloading', speed };
        store.set('download-tasks', currentTasks);
      }
      
      mainWindow.webContents.send('download-update', { type: 'progress', data: { id: task.id, progress, speed, status: 'downloading' } });
    });
    
    await new Promise((resolve, reject) => {
      fileStream.on('finish', () => {
        const finalTasks = store.get('download-tasks', {});
        if (finalTasks[task.id]) {
          finalTasks[task.id].status = 'completed';
          finalTasks[task.id].progress = 100;
          finalTasks[task.id].speed = 0;
          store.set('download-tasks', finalTasks);
        }
        mainWindow.webContents.send('download-update', { type: 'progress', data: { id: task.id, progress: 100, status: 'completed' } });
        resolve();
      });
      
      const errorHandler = (err) => {
        const errorTasks = store.get('download-tasks', {});
        if (errorTasks[task.id]) {
          errorTasks[task.id].status = 'error';
          errorTasks[task.id].error = err.message;
          store.set('download-tasks', errorTasks);
        }
        mainWindow.webContents.send('download-update', { type: 'progress', data: { id: task.id, status: 'error', error: err.message } });
        reject(err);
      };
      
      fileStream.on('error', errorHandler);
      Body.on('error', errorHandler);
    });
  } catch (error) {
    const errorTasks = store.get('download-tasks', {});
    if (errorTasks[task.id]) {
      errorTasks[task.id].status = 'error';
      errorTasks[task.id].error = error.message;
      store.set('download-tasks', errorTasks);
    }
    mainWindow.webContents.send('download-update', { type: 'progress', data: { id: task.id, status: 'error', error: error.message } });
  }
});
```

通过这些优化，下载管理功能现在更加稳定、可靠，并且能够提供更丰富的用户反馈。
<!-- 23c5f93 at https://github.com/JiQingzhe2004/R2APP/commit/23c5f9352c9e4caea7b8dfc2ab487e7b1c75c45e -->

---

## 🚀 更新依赖项与应用功能

本次提交带来了多方面的改进，旨在提升应用的稳定性和用户体验。我们不仅升级了关键的依赖项，还引入了获取应用信息的功能，并新增了关于页面，为用户提供了更全面的应用信息展示。

### 变更摘要

*   **依赖项升级**: 我们将 `lucide-react` 库升级至 `0.525.0` 版本，以利用最新的图标资源和性能优化。这一改动将有助于提升应用的视觉效果和响应速度。
*   **获取应用信息**: 在主进程中添加了 `get-app-info` 功能，允许应用动态获取并返回应用名称、版本、作者、许可证描述等信息。这使得应用能够更灵活地展示自身信息。
*   **新增关于页面**: 我们新增了 `/about` 路由，用户可以通过访问该页面查看应用的详细信息，包括名称、版本、作者、许可证和描述。这一功能增强了应用的透明度和用户友好性。
*   **组件更新**: 侧边栏和头部组件已更新，以支持新功能。特别是头部组件的图标已替换，以匹配新的设计风格。

### 分类和图标

-   `🆕 新功能`: 新增关于页面，展示应用信息。
-   `✨ 功能优化`: 升级 `lucide-react` 至 `0.525.0`，提升图标性能和资源。
-   `🐞 Bug修复`: 无明确bug修复，但依赖项升级可能间接提升稳定性。

### 关键代码展示

```javascript
// 在主进程中添加获取应用信息的功能
import packageJson from '../../package.json' assert { type: 'json' };

ipcMain.handle('get-app-info', () => {
  return {
    name: app.getName(),
    version: app.getVersion(),
    author: packageJson.author,
    description: packageJson.description,
    license: packageJson.license,
  };
});
```

```jsx
// 新增关于页面
export default function AboutPage() {
  const [appInfo, setAppInfo] = useState({
    name: 'R2 存储管理器',
    version: '...',
    author: '...',
    description: '正在加载描述信息...',
    license: '...',
    githubUrl: 'https://github.com/your-repo',
  });

  useEffect(() => {
    window.api.getAppInfo().then(info => {
      setAppInfo(prev => ({ ...prev, ...info }));
    });
  }, []);

  return (
    <div className="p-4 sm:p-6 flex justify-center items-start">
      <Card className="w-full max-w-2xl">
        <CardHeader className="text-center">
          <div className="flex justify-center mb-4">
            <img src={BlackLogo} alt="Logo" className="h-20 w-20 hidden dark:block" />
            <img src={WhiteLogo} alt="Logo" className="h-20 w-20 dark:hidden" />
          </div>
          <CardTitle className="text-3xl font-bold">{appInfo.name}</CardTitle>
        </CardHeader>
        <CardContent className="pt-4 px-8 pb-8 text-sm">
          <p className="text-center mb-8 text-muted-foreground">
            {appInfo.description}
          </p>
          <div className="space-y-5">
            <div className="flex items-center">
              <GitCommit className="h-5 w-5 mr-4 text-muted-foreground" />
              <span className="w-20 text-muted-foreground">版本</span>
              <span className="font-semibold tracking-wider">v {appInfo.version}</span>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
```

通过这些改进，我们不仅提升了应用的性能和稳定性，还为用户提供了更丰富的信息展示和更好的使用体验。
<!-- a14aef5 at https://github.com/JiQingzhe2004/R2APP/commit/a14aef53658ba41cb012d6f4602a8a9192865482 -->

---

## 🚀 添加窗口控制功能

本次提交为应用程序引入了完整的窗口控制功能，包括最小化、最大化和关闭窗口的能力。同时，更新了头部组件以集成窗口控制按钮，并新增了黑白LOGO图标以增强界面视觉效果。

### 变更摘要

`🆕 新功能`

我们为应用程序的用户体验带来了显著的改进，通过添加窗口控制功能，用户现在可以更自由地管理窗口状态。这一改进不仅提升了用户界面的灵活性，还增强了应用程序的专业感。

#### 关键代码变更

**主窗口配置更新:**
```javascript
frame: false, // 移除窗口框架，启用自定义控制
```

**IPC 事件处理:**
```javascript
ipcMain.on('minimize-window', () => {
  mainWindow?.minimize();
});

ipcMain.on('maximize-window', () => {
  if (mainWindow?.isMaximized()) {
    mainWindow.unmaximize();
  } else {
    mainWindow?.maximize();
  }
});

ipcMain.on('close-window', () => {
  mainWindow?.close();
});
```

**预加载脚本更新:**
```javascript
api.minimizeWindow: () => ipcRenderer.send('minimize-window'),
api.maximizeWindow: () => ipcRenderer.send('maximize-window'),
api.closeWindow: () => ipcRenderer.send('close-window'),
```

**头部组件集成:**
```javascript
<div className="flex items-center gap-2" style={{ WebkitAppRegion: 'no-drag' }}>
  <Button variant="ghost" size="icon" className="h-8 w-8" onClick={() => window.api.minimizeWindow()}>
     <Minus className="h-4 w-4" />
  </Button>
  <Button variant="ghost" size="icon" className="h-8 w-8" onClick={() => window.api.maximizeWindow()}>
     <Square className="h-4 w-4" />
  </Button>
  <Button variant="ghost" size="icon" className="h-8 w-8 hover:bg-red-500/90" onClick={() => window.api.closeWindow()}>
     <X className="h-4 w-4" />
  </Button>
</div>
```

**侧边栏LOGO更新:**
```javascript
<img src={BlackLogo} alt="Logo" className="h-6 w-6 hidden dark:block" />
<img src={WhiteLogo} alt="Logo" className="h-6 w-6 dark:hidden" />
```

这些变更不仅增强了用户界面的功能性，还提升了应用程序的整体美观度。通过这些改进，我们确保了应用程序能够更好地满足用户的需求，并提供更加流畅的使用体验。
<!-- f3b89d6 at https://github.com/JiQingzhe2004/R2APP/commit/f3b89d60afd23c38540eb9f84b4f0b1af005161a -->

---

## 🚀 新功能：R2存储配置管理功能

本次提交为应用引入了全新的R2存储配置管理功能，极大地增强了用户在云存储方面的灵活性和便捷性。我们不仅实现了配置文件的添加、删除和切换，还对设置页面的保存逻辑进行了优化，并新增了单选框组件以显著改善用户体验。此外，我们还更新了相关组件，确保它们能够无缝支持这些新功能。

### 🆕 新功能：R2存储配置管理
- **配置文件管理**：用户现在可以轻松添加、删除和切换不同的R2存储配置，使得在不同环境下的切换变得前所未有的简单。
- **设置页面优化**：我们对设置页面的保存逻辑进行了重构，确保用户在保存配置时获得更加流畅和可靠的体验。
- **用户体验改进**：新增单选框组件，让用户在选择默认配置时更加直观和便捷。
- **数据迁移支持**：为了确保老用户能够顺利过渡到新的配置管理系统中，我们添加了数据迁移功能，自动将旧配置转换为新的结构。

### 关键代码片段

```javascript
// Data Migration Function
function runMigration() {
  const oldSettings = store.get('settings');
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

// Enhanced Settings Retrieval
function getActiveSettings() {
  const baseSettings = store.get('settings', {});
  const profiles = store.get('profiles', []);
  const activeProfileId = store.get('activeProfileId');
  const activeProfile = profiles.find(p => p.id === activeProfileId);
  
  if (!activeProfile) {
    return null;
  }
  
  return { ...baseSettings, ...activeProfile };
}
```

通过这些改进，用户现在可以更加高效地管理他们的R2存储配置，同时享受到更加流畅和直观的操作体验。
<!-- 1eba83a at https://github.com/JiQingzhe2004/R2APP/commit/1eba83a27b518e5e1f88c4612242c7c2adc51b75 -->

---

## 🚀 添加R2存储连接状态检查功能

### 变更摘要

本次提交带来了多项重要更新，旨在提升用户体验和系统稳定性。我们引入了R2存储连接状态检查功能，确保用户在操作前存储配置是有效的。同时，我们还优化了设置页面的保存功能，并新增了Tooltip组件以改善整体交互体验。

#### 分类和图标

- `🆕 新功能`: 添加R2存储连接状态检查功能。
- `✨ 功能优化`: 更新相关组件以显示连接状态，优化设置页面保存功能。
- `🐞 Bug修复`: 无明确bug修复记录。
- `🆕 新功能`: 新增Tooltip组件以改善用户体验。

### 关键代码展示

```javascript
// 在electron/main/index.js中添加了新的S3Client导入
import { S3Client, ListObjectsV2Command, DeleteObjectCommand, GetObjectCommand, HeadBucketCommand } from '@aws-sdk/client-s3';

// 新增了check-r2-status IPC处理函数
ipcMain.handle('check-r2-status', async () => {
  const settings = store.get('settings');
  if (!settings || !settings.accountId || !settings.accessKeyId || !settings.secretAccessKey || !settings.bucketName) {
    return { success: false, error: '缺少配置' };
  }

  const s3Client = new S3Client({
    region: 'auto',
    endpoint: `https://${settings.accountId}.r2.cloudflarestorage.com`,
    credentials: {
      accessKeyId: settings.accessKeyId,
      secretAccessKey: settings.secretAccessKey,
    },
  });

  try {
    const command = new HeadBucketCommand({ Bucket: settings.bucketName });
    await s3Client.send(command);
    return { success: true, message: '连接成功' };
  } catch (error) {
    return { success: false, error: `连接失败: ${error.message}` };
  }
});
```

### 新增的依赖

在`package-lock.json`中，我们新增了`@radix-ui/react-tooltip`依赖，以支持Tooltip组件的引入：

```json
"@radix-ui/react-tooltip": "^1.2.7",
```

这些变更将显著提升用户在使用R2存储时的体验，确保操作的可靠性和便捷性。
<!-- 1a7daa7 at https://github.com/JiQingzhe2004/R2APP/commit/1a7daa75a3aabaae5ff706dfaf37009fdc72eaab -->

---

## 🚀 新功能：添加搜索对话框功能

### 变更摘要

本次提交为应用引入了全新的**搜索对话框功能**，并对文件页面的搜索逻辑进行了深度优化。我们重新设计了文件列表和搜索结果的展示方式，并改进了删除确认提示信息，以提供更流畅、更直观的用户体验。

#### 主要变更点：

*   **🆕 新功能**：添加了搜索对话框组件，允许用户在文件页面中快速查找文件。
*   **✨ 功能优化**：优化了文件页面的搜索逻辑，提升了搜索效率和准确性。
*   **✨ 功能优化**：调整了文件列表和搜索结果的显示方式，使其更加清晰和易于使用。
*   **🐞 Bug修复**：改进了删除确认提示信息，确保用户在执行删除操作前能够获得明确的确认提示。

### 关键代码展示

以下是最关键的代码修改，展示了如何实现搜索对话框功能：

```jsx
// App.jsx
import { useState } from 'react';
import Header from './components/header.jsx';

function App() {
  const [isSidebarCollapsed, setIsSidebarCollapsed] = useState(false);
  const [isSearchDialogOpen, setIsSearchDialogOpen] = useState(false);

  // ... 其他代码 ...

  return (
    <Layout>
      <Sidebar isCollapsed={isSidebarCollapsed} onToggle={toggleSidebar} />
      <LayoutBody>
        <Header onSearchClick={() => setIsSearchDialogOpen(true)} />
        {/* ... 其他代码 ... */}
      </LayoutBody>
    </Layout>
  );
}
```

```jsx
// components/header.jsx
import { Button, TextSearch } from '@/components/ui/Button';
import { useLocation } from 'react-router-dom';

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
      {/* ... 其他代码 ... */}
    </header>
  );
}
```

```jsx
// pages/Files.jsx
import { Dialog, DialogContent, DialogHeader, DialogTitle } from "@/components/ui/dialog";

export default function FilesPage({ isSearchOpen, onSearchOpenChange }) {
  // ... 其他代码 ...

  return (
    <Dialog open={isSearchOpen} onOpenChange={onSearchOpenChange}>
      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle>搜索文件</DialogTitle>
        </DialogHeader>
        {/* ... 其他代码 ... */}
      </DialogContent>
    </Dialog>
  );
}
```

这些修改确保了搜索对话框能够在文件页面中正确显示，并允许用户通过输入关键词来搜索文件。同时，我们还优化了删除确认提示信息，以确保用户在执行删除操作前能够获得明确的确认提示。

### 总结

本次提交为应用引入了全新的搜索对话框功能，并对文件页面的搜索逻辑进行了深度优化。这些改进将大大提升用户在文件管理方面的体验，使文件查找和操作更加高效和便捷。
<!-- 5ba7e66 at https://github.com/JiQingzhe2004/R2APP/commit/5ba7e660427fe2174b572bdefe77dd2ff51ee49f -->

---

## 🚀 更新依赖项与功能增强

本次提交带来了多方面的改进，旨在提升应用的稳定性和用户体验。我们不仅更新了关键依赖项，还引入了文件搜索功能，并对文件列表加载逻辑进行了优化。此外，删除确认提示和搜索结果提示信息也得到了改进，使操作更加直观和安全。

### ✨ 功能优化

- **文件搜索功能新增**: 引入了强大的文件搜索功能，让用户能够快速定位所需文件。这一功能极大地提升了应用的实用性，特别是在处理大量文件时。
- **文件列表加载逻辑优化**: 对文件列表加载逻辑进行了优化，确保在处理大量文件时，应用依然保持流畅的响应速度。这一改进将显著提升用户体验，尤其是在网络环境不佳的情况下。
- **删除确认提示改进**: 删除确认提示得到了改进，现在用户在执行删除操作时，会收到更加明确的确认信息，从而避免误操作。

### 🆕 新功能

- **文件搜索功能**: 新增的文件搜索功能允许用户通过关键词快速搜索文件，极大地提高了工作效率。

### 🐞 Bug修复

- **依赖项更新**: 更新了多个关键依赖项，修复了潜在的bug，并提升了应用的整体稳定性。

### 代码示例

以下是一些关键代码的节选，展示了新增的文件搜索功能和删除确认提示的改进：

```javascript
// electron/main/index.js
ipcMain.handle('r2-list-objects', async (_, { continuationToken, prefix }) => {
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
});
```

```javascript
// electron/preload/index.mjs
const api = {
  listObjects: ({ continuationToken, prefix }) => ipcRenderer.invoke('r2-list-objects', { continuationToken, prefix }),
  deleteObject: (key) => ipcRenderer.invoke('r2-delete-object', key),
  // 其他API方法...
};
```

通过这些改进，我们确保了应用的稳定性和用户体验得到了显著提升。感谢所有贡献者的努力，让我们共同推动项目不断前进！
<!-- aab3f96 at https://github.com/JiQingzhe2004/R2APP/commit/aab3f96c5dca6d322e3f2335f804f24269403e1a -->

---

## 🚀 更新依赖项与文件管理功能

本次提交带来了多项重要更新，旨在提升应用的**文件上传与下载**体验，并引入了全新的**下载管理页面**。以下是本次变更的详细内容：

### **变更摘要**

*   **添加下载管理页面**：现在用户可以实时监控文件下载状态，包括进度、速度和错误信息。页面还支持取消下载和清除已完成任务，极大地提升了文件管理的便捷性。
*   **优化文件上传与下载功能**：
    *   **上传**：通过AWS SDK的`Upload`类，实现了更精细的上传控制，包括分片上传（`partSize`）、并发控制（`queueSize`）和实时进度反馈。上传过程中，主窗口会实时显示上传百分比，让用户清晰掌握进度。
    *   **下载**：引入了完整的下载任务状态管理（`starting`、`downloading`、`completed`、`error`），并记录了下载速度。下载完成后自动重命名文件，避免覆盖同名文件。
*   **改进文件页面的显示逻辑**：通过`@aws-sdk/client-s3`的`GetObjectCommand`获取文件元数据，并计划后续添加**文件类型图标和描述**，提升文件的可识别性。
*   **依赖项更新**：引入了`uuid`库用于生成唯一的下载任务ID，并更新了`path`模块的导入，增加了`parse`函数支持。

### **分类与图标**

*   `🆕 新功能`：下载管理页面、文件下载状态管理、实时下载进度反馈。
*   `✨ 功能优化`：文件上传分片与并发控制、下载速度统计、文件重命名逻辑。
*   `🐞 Bug修复`：解决了下载任务在文件存在时可能被覆盖的问题。
*   `其他`：依赖项更新、代码结构优化。

### **关键代码示例**

#### **上传进度实时反馈**

```javascript
upload.on('httpUploadProgress', (progress) => {
  if (progress.total) {
    const percentage = Math.round((progress.loaded / progress.total) * 100);
    mainWindow.webContents.send('upload-progress', { key, percentage });
  }
});
```

#### **下载任务状态管理**

```javascript
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

// 更新下载任务状态
task.status = 'downloading';
task.total = ContentLength;
```

#### **下载速度统计**

```javascript
let lastProgressTime = Date.now();
let lastDownloaded = 0;

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
```

通过这些改进，应用现在能够提供更稳定、更透明的文件管理体验，同时增强了用户对下载过程的掌控力。
<!-- ca00387 at https://github.com/JiQingzhe2004/R2APP/commit/ca00387ae115afc12e8c76c3554ff54675a9b43b -->

---

## ✨ 功能优化

本次提交带来了多方面的功能优化和改进，旨在提升用户体验和应用性能。我们引入了新的依赖项，增强了快捷键功能，改进了侧边栏的折叠交互，并优化了文件页面的加载逻辑。同时，还在设置页面中集成了toast通知，以提供更及时的反馈。

### 🆕 新功能
- **添加sonner库**: 引入了`sonner`库，用于在设置页面中提供toast通知，增强用户操作的即时反馈。
- **注册F5快捷键**: 在主进程中注册了F5快捷键，用于刷新窗口，提升操作便捷性。

### ✨ 功能优化
- **改进侧边栏折叠功能**: 优化了侧边栏的折叠交互，使其更加流畅和直观。
- **优化文件页面加载逻辑**: 改进了文件页面的加载和显示逻辑，提升了页面加载速度和用户体验。
- **集成toast通知**: 在设置页面中集成了toast通知，用于反馈连接和保存状态，增强用户操作的即时反馈。

### 关键代码展示

#### 注册F5快捷键
```javascript
app.whenReady().then(() => {
  // Register F5 for refresh
  globalShortcut.register('F5', () => {
    const focusedWindow = BrowserWindow.getFocusedWindow();
    if (focusedWindow) {
      focusedWindow.webContents.reload();
    }
  });
});
```

#### 侧边栏折叠功能
```javascript
export function Sidebar({ isCollapsed, onToggle }) {
  const { theme, setTheme } = useTheme();
  const location = useLocation();

  const navItems = [
    { id: 'dashboard', href: '/dashboard', icon: Home, label: '仪表盘' },
    { id: 'files', href: '/files', icon: PackageOpen, label: '文件管理' },
    { id: 'uploads', href: '/uploads', icon: FolderUp, label: '上传文件' },
    { id: 'downloads', href: '#', icon: FolderDown, label: '下载管理', disabled: true },
    { id: 'settings', href: '/settings', icon: Settings, label: '设置' },
  ];

  return (
    <aside className={cn(
      "flex-shrink-0 border-r bg-muted/40 flex flex-col transition-all duration-300 ease-in-out",
      isCollapsed ? "w-20" : "w-64"
    )}>
      <div className={cn(
        "h-14 flex items-center border-b px-6",
        isCollapsed && "px-0 justify-center"
      )}>
        <h1 className={cn("text-lg font-bold", isCollapsed && "hidden")}>R2存储管理器</h1>
        <h1 className={cn("text-lg font-bold", !isCollapsed && "hidden")}>R2</h1>
      </div>
      <nav className="flex-1 py-4 px-4">
        <ul className="space-y-1 h-full flex flex-col">
          {navItems.map(({ id, href, icon: Icon, label, disabled }) => {
            const isActive = location.pathname === href;
            const isSettings = id === 'settings';
            const liClass = isSettings ? 'mt-auto' : '';

            const linkContent = (
              <>
                <Icon className={cn("h-5 w-5", isCollapsed && "h-6 w-6")} />
                <span className={cn(isCollapsed && "hidden")}>
                  {label}
                  {disabled && ' (待开发)'}
                </span>
              </>
            );

            return (
              <li key={id} className={liClass}>
                {disabled ? (
                  <span
                    className={cn(
                      "flex items-center gap-3 rounded-lg px-3 py-2 text-muted-foreground opacity-50 cursor-not-allowed",
                      isCollapsed && "justify-center"
                    )}
                  >
                    {linkContent}
                  </span>
                ) : (
                  <Link to={href} className={cn("flex items-center gap-3 rounded-lg px-3 py-2 text-muted-foreground hover:bg-accent hover:text-accent-foreground", isActive && "bg-accent text-accent-foreground")}>
                    {linkContent}
                  </Link>
                )}
              </li>
            );
          })}
        </ul>
      </nav>
    </aside>
  );
}
```

通过这些改进，我们不仅提升了应用的功能性和用户体验，还增强了应用的稳定性和性能。
<!-- 367d89f at https://github.com/JiQingzhe2004/R2APP/commit/367d89f63d2af19eba08e01d7fb1b23ed5490c6f -->

---

## 🐞 Bug修复

本次提交解决了存储桶应用在构建后无法正常运行的问题。通过在开发环境中运行应用程序，我们识别到应用在构建过程中缺少必要的文件和配置，导致在非开发环境下无法正常启动。以下是本次修复的关键变更：

### 🚀 变更摘要

*   **修复构建后运行问题**: 我们在 `.gitignore` 文件中添加了必要的构建输出目录和配置文件，确保在构建过程中不会意外删除关键文件。
*   **增强开发体验**: 通过在 `electron.vite.config.js` 中配置 `electron-serve`，我们优化了开发环境的启动流程，并添加了详细的日志记录，以便更轻松地调试文件请求和加载问题。
*   **改进错误处理**: 在 `electron/main/index.js` 中，我们增强了错误处理逻辑，添加了对 `dist` 目录和 `index.html` 文件的存在性检查，并在加载失败时提供更详细的错误信息。

### 🆕 新功能

*   **添加 `.gitignore` 配置**: 确保构建输出目录（如 `out`、`dist`、`release`）和开发环境配置文件（如 `.vscode`）不会被意外提交到版本控制中。
*   **配置 `electron-serve`**: 通过 `electron.vite.config.js` 中的配置，我们实现了更简洁的开发环境启动流程，并提供了详细的日志记录功能。

### 关键代码示例

#### `.gitignore` 新增配置
```markdown
node_modules
.vscode
out
dist
release
```

#### `electron.vite.config.js` 配置 `electron-serve`
```javascript
const loadURL = serve({
  directory: 'dist',
  handler: (request, response) => {
    const url = request.url.replace('app://', '');
    console.log(`[electron-serve] Request for: ${url}`);
    return null;
  }
});
```

#### `electron/main/index.js` 增强的错误处理
```javascript
mainWindow.webContents.on('did-fail-load', (event, errorCode, errorDescription, validatedURL) => {
  console.error(`Failed to load URL: ${validatedURL}`);
  console.error(`Error code: ${errorCode}, Description: ${errorDescription}`);
});
```

### 📦 整体改进

通过这些变更，我们现在确保了应用在构建后能够在非开发环境下正常运行，同时提供了更好的开发体验和错误调试能力。这些改进将显著提升开发效率和应用的稳定性。
<!-- 860c023 at https://github.com/JiQingzhe2004/R2APP/commit/860c023f2ccd8321c602da0d7cf5a28014ffb378 -->