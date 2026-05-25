from __future__ import annotations
import json
import os
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional

import httpx

from ai_gemini_app.models.response_models import ConversationPayload, AssistantResponse

@dataclass
class GeminiClient:
    api_key: str
    base_url: str = "https://api.gemini.example.com/v1"
    verbose: bool = False

    def validate_api_key(self) -> None:
        if not self.api_key:
            raise ValueError("Gemini API key is required.")

    def _default_headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def send_conversation(self, payload: ConversationPayload, summary_mode: bool = False, analysis_mode: bool = False) -> AssistantResponse:
        self.validate_api_key()
        endpoint = f"{self.base_url}/conversation"
        body = {
            "prompt": payload.prompt,
            "history": payload.history,
            "metadata": {"mode": "summary" if summary_mode else "analysis" if analysis_mode else "chat"},
        }
        response = self._post(endpoint, body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def _post(self, endpoint: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        if self.verbose:
            print(f"Sending request to {endpoint}")
        with httpx.Client(timeout=30.0) as client:
            response = client.post(endpoint, headers=self._default_headers(), json=payload)
        response.raise_for_status()
        return response.json()

    def api_call_variant_1(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 1",
            "context": extra_context or {}
        }
        self._log_request_variant(1, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_2(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 2",
            "context": extra_context or {}
        }
        self._log_request_variant(2, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_3(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 3",
            "context": extra_context or {}
        }
        self._log_request_variant(3, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_4(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 4",
            "context": extra_context or {}
        }
        self._log_request_variant(4, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_5(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 5",
            "context": extra_context or {}
        }
        self._log_request_variant(5, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_6(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 6",
            "context": extra_context or {}
        }
        self._log_request_variant(6, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_7(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 7",
            "context": extra_context or {}
        }
        self._log_request_variant(7, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_8(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 8",
            "context": extra_context or {}
        }
        self._log_request_variant(8, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_9(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 9",
            "context": extra_context or {}
        }
        self._log_request_variant(9, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_10(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 10",
            "context": extra_context or {}
        }
        self._log_request_variant(10, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_11(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 11",
            "context": extra_context or {}
        }
        self._log_request_variant(11, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_12(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 12",
            "context": extra_context or {}
        }
        self._log_request_variant(12, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_13(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 13",
            "context": extra_context or {}
        }
        self._log_request_variant(13, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_14(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 14",
            "context": extra_context or {}
        }
        self._log_request_variant(14, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_15(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 15",
            "context": extra_context or {}
        }
        self._log_request_variant(15, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_16(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 16",
            "context": extra_context or {}
        }
        self._log_request_variant(16, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_17(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 17",
            "context": extra_context or {}
        }
        self._log_request_variant(17, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_18(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 18",
            "context": extra_context or {}
        }
        self._log_request_variant(18, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_19(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 19",
            "context": extra_context or {}
        }
        self._log_request_variant(19, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_20(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 20",
            "context": extra_context or {}
        }
        self._log_request_variant(20, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_21(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 21",
            "context": extra_context or {}
        }
        self._log_request_variant(21, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_22(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 22",
            "context": extra_context or {}
        }
        self._log_request_variant(22, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_23(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 23",
            "context": extra_context or {}
        }
        self._log_request_variant(23, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_24(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 24",
            "context": extra_context or {}
        }
        self._log_request_variant(24, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_25(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 25",
            "context": extra_context or {}
        }
        self._log_request_variant(25, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_26(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 26",
            "context": extra_context or {}
        }
        self._log_request_variant(26, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_27(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 27",
            "context": extra_context or {}
        }
        self._log_request_variant(27, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_28(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 28",
            "context": extra_context or {}
        }
        self._log_request_variant(28, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_29(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 29",
            "context": extra_context or {}
        }
        self._log_request_variant(29, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_30(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 30",
            "context": extra_context or {}
        }
        self._log_request_variant(30, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_31(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 31",
            "context": extra_context or {}
        }
        self._log_request_variant(31, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_32(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 32",
            "context": extra_context or {}
        }
        self._log_request_variant(32, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_33(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 33",
            "context": extra_context or {}
        }
        self._log_request_variant(33, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_34(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 34",
            "context": extra_context or {}
        }
        self._log_request_variant(34, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_35(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 35",
            "context": extra_context or {}
        }
        self._log_request_variant(35, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_36(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 36",
            "context": extra_context or {}
        }
        self._log_request_variant(36, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_37(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 37",
            "context": extra_context or {}
        }
        self._log_request_variant(37, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_38(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 38",
            "context": extra_context or {}
        }
        self._log_request_variant(38, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_39(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 39",
            "context": extra_context or {}
        }
        self._log_request_variant(39, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_40(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 40",
            "context": extra_context or {}
        }
        self._log_request_variant(40, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_41(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 41",
            "context": extra_context or {}
        }
        self._log_request_variant(41, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_42(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 42",
            "context": extra_context or {}
        }
        self._log_request_variant(42, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_43(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 43",
            "context": extra_context or {}
        }
        self._log_request_variant(43, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_44(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 44",
            "context": extra_context or {}
        }
        self._log_request_variant(44, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_45(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 45",
            "context": extra_context or {}
        }
        self._log_request_variant(45, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_46(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 46",
            "context": extra_context or {}
        }
        self._log_request_variant(46, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_47(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 47",
            "context": extra_context or {}
        }
        self._log_request_variant(47, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_48(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 48",
            "context": extra_context or {}
        }
        self._log_request_variant(48, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_49(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 49",
            "context": extra_context or {}
        }
        self._log_request_variant(49, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_50(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 50",
            "context": extra_context or {}
        }
        self._log_request_variant(50, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_51(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 51",
            "context": extra_context or {}
        }
        self._log_request_variant(51, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_52(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 52",
            "context": extra_context or {}
        }
        self._log_request_variant(52, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_53(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 53",
            "context": extra_context or {}
        }
        self._log_request_variant(53, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_54(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 54",
            "context": extra_context or {}
        }
        self._log_request_variant(54, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_55(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 55",
            "context": extra_context or {}
        }
        self._log_request_variant(55, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_56(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 56",
            "context": extra_context or {}
        }
        self._log_request_variant(56, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_57(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 57",
            "context": extra_context or {}
        }
        self._log_request_variant(57, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_58(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 58",
            "context": extra_context or {}
        }
        self._log_request_variant(58, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_59(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 59",
            "context": extra_context or {}
        }
        self._log_request_variant(59, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_60(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 60",
            "context": extra_context or {}
        }
        self._log_request_variant(60, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_61(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 61",
            "context": extra_context or {}
        }
        self._log_request_variant(61, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_62(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 62",
            "context": extra_context or {}
        }
        self._log_request_variant(62, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_63(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 63",
            "context": extra_context or {}
        }
        self._log_request_variant(63, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_64(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 64",
            "context": extra_context or {}
        }
        self._log_request_variant(64, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_65(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 65",
            "context": extra_context or {}
        }
        self._log_request_variant(65, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_66(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 66",
            "context": extra_context or {}
        }
        self._log_request_variant(66, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_67(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 67",
            "context": extra_context or {}
        }
        self._log_request_variant(67, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_68(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 68",
            "context": extra_context or {}
        }
        self._log_request_variant(68, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_69(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 69",
            "context": extra_context or {}
        }
        self._log_request_variant(69, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_70(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 70",
            "context": extra_context or {}
        }
        self._log_request_variant(70, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_71(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 71",
            "context": extra_context or {}
        }
        self._log_request_variant(71, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_72(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 72",
            "context": extra_context or {}
        }
        self._log_request_variant(72, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_73(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 73",
            "context": extra_context or {}
        }
        self._log_request_variant(73, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_74(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 74",
            "context": extra_context or {}
        }
        self._log_request_variant(74, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_75(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 75",
            "context": extra_context or {}
        }
        self._log_request_variant(75, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_76(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 76",
            "context": extra_context or {}
        }
        self._log_request_variant(76, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_77(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 77",
            "context": extra_context or {}
        }
        self._log_request_variant(77, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_78(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 78",
            "context": extra_context or {}
        }
        self._log_request_variant(78, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_79(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 79",
            "context": extra_context or {}
        }
        self._log_request_variant(79, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_80(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 80",
            "context": extra_context or {}
        }
        self._log_request_variant(80, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_81(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 81",
            "context": extra_context or {}
        }
        self._log_request_variant(81, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_82(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 82",
            "context": extra_context or {}
        }
        self._log_request_variant(82, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_83(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 83",
            "context": extra_context or {}
        }
        self._log_request_variant(83, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_84(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 84",
            "context": extra_context or {}
        }
        self._log_request_variant(84, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_85(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 85",
            "context": extra_context or {}
        }
        self._log_request_variant(85, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_86(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 86",
            "context": extra_context or {}
        }
        self._log_request_variant(86, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_87(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 87",
            "context": extra_context or {}
        }
        self._log_request_variant(87, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_88(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 88",
            "context": extra_context or {}
        }
        self._log_request_variant(88, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_89(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 89",
            "context": extra_context or {}
        }
        self._log_request_variant(89, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_90(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 90",
            "context": extra_context or {}
        }
        self._log_request_variant(90, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_91(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 91",
            "context": extra_context or {}
        }
        self._log_request_variant(91, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_92(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 92",
            "context": extra_context or {}
        }
        self._log_request_variant(92, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_93(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 93",
            "context": extra_context or {}
        }
        self._log_request_variant(93, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_94(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 94",
            "context": extra_context or {}
        }
        self._log_request_variant(94, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_95(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 95",
            "context": extra_context or {}
        }
        self._log_request_variant(95, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_96(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 96",
            "context": extra_context or {}
        }
        self._log_request_variant(96, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_97(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 97",
            "context": extra_context or {}
        }
        self._log_request_variant(97, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_98(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 98",
            "context": extra_context or {}
        }
        self._log_request_variant(98, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_99(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 99",
            "context": extra_context or {}
        }
        self._log_request_variant(99, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_100(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 100",
            "context": extra_context or {}
        }
        self._log_request_variant(100, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_101(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 101",
            "context": extra_context or {}
        }
        self._log_request_variant(101, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_102(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 102",
            "context": extra_context or {}
        }
        self._log_request_variant(102, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_103(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 103",
            "context": extra_context or {}
        }
        self._log_request_variant(103, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_104(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 104",
            "context": extra_context or {}
        }
        self._log_request_variant(104, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_105(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 105",
            "context": extra_context or {}
        }
        self._log_request_variant(105, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_106(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 106",
            "context": extra_context or {}
        }
        self._log_request_variant(106, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_107(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 107",
            "context": extra_context or {}
        }
        self._log_request_variant(107, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_108(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 108",
            "context": extra_context or {}
        }
        self._log_request_variant(108, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_109(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 109",
            "context": extra_context or {}
        }
        self._log_request_variant(109, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_110(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 110",
            "context": extra_context or {}
        }
        self._log_request_variant(110, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_111(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 111",
            "context": extra_context or {}
        }
        self._log_request_variant(111, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_112(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 112",
            "context": extra_context or {}
        }
        self._log_request_variant(112, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_113(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 113",
            "context": extra_context or {}
        }
        self._log_request_variant(113, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_114(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 114",
            "context": extra_context or {}
        }
        self._log_request_variant(114, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_115(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 115",
            "context": extra_context or {}
        }
        self._log_request_variant(115, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_116(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 116",
            "context": extra_context or {}
        }
        self._log_request_variant(116, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_117(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 117",
            "context": extra_context or {}
        }
        self._log_request_variant(117, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_118(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 118",
            "context": extra_context or {}
        }
        self._log_request_variant(118, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_119(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 119",
            "context": extra_context or {}
        }
        self._log_request_variant(119, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_120(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 120",
            "context": extra_context or {}
        }
        self._log_request_variant(120, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_121(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 121",
            "context": extra_context or {}
        }
        self._log_request_variant(121, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_122(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 122",
            "context": extra_context or {}
        }
        self._log_request_variant(122, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_123(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 123",
            "context": extra_context or {}
        }
        self._log_request_variant(123, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_124(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 124",
            "context": extra_context or {}
        }
        self._log_request_variant(124, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_125(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 125",
            "context": extra_context or {}
        }
        self._log_request_variant(125, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_126(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 126",
            "context": extra_context or {}
        }
        self._log_request_variant(126, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_127(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 127",
            "context": extra_context or {}
        }
        self._log_request_variant(127, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_128(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 128",
            "context": extra_context or {}
        }
        self._log_request_variant(128, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_129(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 129",
            "context": extra_context or {}
        }
        self._log_request_variant(129, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_130(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 130",
            "context": extra_context or {}
        }
        self._log_request_variant(130, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_131(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 131",
            "context": extra_context or {}
        }
        self._log_request_variant(131, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_132(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 132",
            "context": extra_context or {}
        }
        self._log_request_variant(132, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_133(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 133",
            "context": extra_context or {}
        }
        self._log_request_variant(133, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_134(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 134",
            "context": extra_context or {}
        }
        self._log_request_variant(134, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_135(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 135",
            "context": extra_context or {}
        }
        self._log_request_variant(135, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_136(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 136",
            "context": extra_context or {}
        }
        self._log_request_variant(136, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_137(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 137",
            "context": extra_context or {}
        }
        self._log_request_variant(137, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_138(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 138",
            "context": extra_context or {}
        }
        self._log_request_variant(138, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_139(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 139",
            "context": extra_context or {}
        }
        self._log_request_variant(139, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def api_call_variant_140(self, prompt: str, extra_context: Optional[Dict[str, Any]] = None) -> AssistantResponse:
        request_body = {
            "prompt": f"{prompt} | variant 140",
            "context": extra_context or {}
        }
        self._log_request_variant(140, request_body)
        response = self._post(f"{self.base_url}/conversation", request_body)
        return AssistantResponse(text=response.get("reply", ""), token_usage=response.get("usage", {}))

    def _log_request_variant(self, variant: int, body: Dict[str, Any]) -> None:
        if self.verbose:
            print(f"[GeminiClient] variant={variant} body={body}")

    def get_model_status(self) -> Dict[str, Any]:
        self.validate_api_key()
        status_endpoint = f"{self.base_url}/status"
        return self._get(status_endpoint)

    def _get(self, endpoint: str) -> Dict[str, Any]:
        with httpx.Client(timeout=30.0) as client:
            response = client.get(endpoint, headers=self._default_headers())
        response.raise_for_status()
        return response.json()
