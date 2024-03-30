import gradio as gr
from face_compare import FaceCompare
from face_feature_analysis import FaceFeature

appid = 'b6673a3a'
api_secret = 'YzZhZDE3ZDI3Mjc4ZDI2NzJjMWMxZDU5'
api_key = 'f65a0459f9e14b1faa052952376a3f5d'


with gr.Blocks() as demo:
    with gr.Tab("人脸比对"):
        with gr.Row():
            pic1 = gr.Image(label="图片1", type="filepath")
            pic2 = gr.Image(label="图片2", type="filepath")
        with gr.Row():
            result = gr.Textbox(label="比对结果")
            compare = gr.Button(value="开始比对")

            def display_compare(data):
                res = f"可信度: {data['score']}\n结果: {data['desc']}"
                return res

            @compare.click(inputs=[pic1,pic2], outputs=result)
            def face_compare(img1_path, img2_path):
                res = FaceCompare(appid, api_secret, api_key, img1_path, img2_path).run()
                res = display_compare(res)
                return res


    with gr.Tab("人脸特征分析"):
        with gr.Row():
            img = gr.Image(label="分析图片", type='filepath')
            result = gr.TextArea(label="分析结果")
        analyze = gr.Button(value="开始分析")

        def display_analyze(data):
            result = ""
            for item in data:
                result += f"{item['type']}: {item['desc']}\n"
            return result

        @analyze.click(inputs=img, outputs=result)
        def face_analyze(img_path):
            api_key = "8e5b3958f8e856863ca8c43c2a0a2aab"
            res = FaceFeature(appid, api_key, img_path).face_local_analysis()
            res = display_analyze(res)
            return res

demo.launch()